

# ===============
# 特定フォノンモードの向きにそって変位させたPOSCARを作成する．
# ===============



import numpy as np
ang_to_bohr=1.8897259886 

# parserの設定

import argparse    # 1. argparseをインポート

parser = argparse.ArgumentParser(description='calculate displacement POSCAR')    # 2. パーサを作る

# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument('arg1', help='VASP POSCAR-type file',default='POSCAR')    # 必須の引数を追加
parser.add_argument('arg2', help='ALAMODE-type eigenvector file', default="mode.txt")
parser.add_argument('--disp',help="displacement size in Ang", type=float, default="0.01")    # オプション引数（指定しなくても良い引数）を追加(type=で型指定)
# parser.add_argument('-a', '--arg4')   # よく使う引数なら省略形があると使う時に便利

args = parser.parse_args()    # 4. 引数を解析

print('arg1='+args.arg1)
print('arg2='+args.arg2)
print('disp='+str(args.disp))
# print('arg4='+args.arg4)


VASP_input=args.arg1
mode_input=args.arg2
displacement_size=args.disp



# 座標をリスト形式で読み込み
def read_POSCAR(VASP_input):
    import numpy as np

    lines=[]
    counter=0 # カウンタ
    coord=[]
    #
    #
    with open(VASP_input, "r") as tf:
        for line in tf:
            # まずは結晶構造の読み込み
            if counter == 1: # a0
                l1=line
                a0=float(l1)
            if counter == 2: #a1
                tmp=line.split()
                a1=np.array([float(tmp[0]),float(tmp[1]),float(tmp[2])])
            if counter == 3: #a2
                tmp=line.split()
                a2=np.array([float(tmp[0]),float(tmp[1]),float(tmp[2])])
            if counter == 4: #a3
                tmp=line.split()
                a3=np.array([float(tmp[0]),float(tmp[1]),float(tmp[2])])
            # 次に分子の種類の読み込み
            if counter == 5: #a1
                atoms=line.split()
            if counter == 6: #a1
                atoms_num=line.split()
            # 最後にion座標のよみこみ
            if counter >= 8: #a1
                tmp=line.split()
                coord.append([float(tmp[0]),float(tmp[1]),float(tmp[2])])
                #
                #
            #print(line.split())
            #print(tf.readline())
            # .split()
            counter= counter+1
    #
    #最後の調整
    coord=np.array(coord)
    #print(np.shape(lines))
    #print(lines)
    #print(coord)

    # 結晶ベクトル (これはAngstrom単位？)
    a1=a0*a1
    a2=a0*a2
    a3=a0*a3
    return coord,a1,a2,a3


def read_mode(mode_input):
    # mode.txtを読み込み
    eigen_mode=np.loadtxt(mode_input)[:,0].reshape([-1,3]) # print(eigen_mode)
    
    # 最大の長さを持つ変位で割る．
    max_ling=np.amax(np.abs(eigen_mode)) #print(max_ling)
    eigen_mode=eigen_mode/max_ling
    
    return eigen_mode


def calc_fractional_mode(a1,a2,a3,eigen_mode):    
    # 
    # eigen_modeの座標を結晶座標に変換 
    # https://chemistry.stackexchange.com/questions/136836/converting-fractional-coordinates-into-cartesian-coordinates-for-crystallography
    # 結晶座標
    A = np.vstack([a1, a2, a3]).T    # print(A)

    # eigen_mode(デカルト座標)
    x = eigen_mode.T    # print(x)

    # eigen_mode(結晶座標)
    y = np.matmul(np.linalg.inv(A),x).T    # print(a*y.T)

    return y


def calc_output(coord, eigen_mode_frac, displacement_size):
    # eigen_mode_frac: fractional座標の固有ベクトル
    #
    #
    # a=0.005 # ang(変位)
    # a=ang_to_bohr*a #bohr
    print("")
    print("displacement in Angstrom... = ",displacement_size)
    print("")
    # 
    # 長さ調整した固有ベクトルを座標データに加える
    output=coord+displacement_size*eigen_mode_frac
    # 
    for i,vec in enumerate(output):
        print(vec)
    return output


def process(VASP_input, mode_input,displacement_size):
    # read POSCAR
    coord,a1,a2,a3=read_POSCAR(VASP_input)
    #
    # read mode.in
    eigen_mode = read_mode(mode_input)
    #
    # calclate fractional coord of eigen_mode
    eigen_mode_frac = calc_fractional_mode(a1,a2,a3,eigen_mode)
    #
    # calc final coord
    final_poscar = calc_output(coord,eigen_mode_frac,displacement_size)
    # 
    return final_poscar


if __name__ == '__main__':
    '''
    Simple script for making poscar with displacement of a specific phonon-mode.
    Usage:
    $ python make_modedisp.py POSCAR mode.in displacement
    
    For details of available options, please type
    $ python make_modedisp.py -h
    '''
    process(VASP_input, mode_input,displacement_size)
    
    
