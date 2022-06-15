#!/usr/bin/env python3


# ===================
# 
# ===================
# Time-stamp: <2022-06-16 00:32:09 amanotomohito>


import numpy as np

# ====================
# parserの設定

import argparse    # 1. argparseをインポート

parser = argparse.ArgumentParser(description='convert SPOSCAR to suggest.in ')    # 2. パーサを作る

# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument('arg1', help='VASP POSCAR-type file',default='SPOSCAR')    # 必須の引数を追加
parser.add_argument('arg2', help='ALAMODE-type output file', default="sugeest.in")
# parser.add_argument('-a', '--arg4')   # よく使う引数なら省略形があると使う時に便利




def read_write(VASP_input, ALM_output):
  import linecache
  #
  f   = open(VASP_input, 'r') # read SPOSCAR
  f2  = open(ALM_output, "w") # output suggest.in

  # カウンター
  counter=0  #行数をカウント
  counter2=0 #原子数カウント
  # 
  f2.write("&general \n")
  f2.write("PREFIX = suggest\n")
  f2.write(" MODE = suggest \n")

  # 最初にNAT/NKD/KDを取得しておく
  KD = linecache.getline(VASP_input, 6) # atomic species
  NKD = len(KD.split())                 # # of species
  NAT_str = linecache.getline(VASP_input, 7).split()
  NAT = np.sum(np.array([int(s) for s in NAT_str])) # # of atoms
  # https://qiita.com/Kodaira_/items/eb5cdef4c4e299794be3
  linecache.clearcache() 
  #
  f2.write(" NAT = "+ str(NAT) + " \n")
  f2.write(" NKD = "+ str(NKD) + " \n")
  f2.write(" KD = "+KD+" \n")
  f2.write("/\n")
  #
  #
  while True:
    data = f.readline()
    # dataが空行になったら出る．POSCARには速度情報が入ることがあるのでこれを除去するため．
    # 単にdata=="\n"だと"  \n"のような場合を排除できないので，splitするのが確実．
    if data.split() == []: 
      break
    # debug:: print(data.split())
    ##
    ##
    if counter==2:
      f2.write("&interaction\n")
      f2.write("NORDER = 1  # 1: harmonic, 2: cubic, ..\n")
      f2.write("/\n")
      f2.write("&cell\n")
      f2.write("1.8897259886\n")  # convert from bohr to Ang
    #
    ## lattice constantを出力
    if counter==2 or counter==3 or counter==4:
        f2.write(data)  #print (data)
    #
    if counter==4:
      f2.write("/\n")
      f2.write("&cutoff\n")
      f2.write("*-* None\n")
      f2.write("/\n")
      f2.write("&position\n")
    #
    ## 各原子の数をget
    if counter==6:
      num_spices=data.strip("\n").split()
      num_atoms=[int(i) for i in num_spices] 
      #print("原子種")
      #print(num_atoms)
      # num_atomに沿ったリストを作成( 1スタートなのでi+1になっている)
      ans=[int(i)+1 for i,num in enumerate(num_atoms) for k in range(num) ]
    #
    ## 座標を出力
    if counter >= 8:
      f2.write(str(ans[counter2])+" "+ data)
      counter2=counter2+1
    # 
    counter=counter+1

  f.close()
  f2.close()
  # 成功チェック
  if counter2 == np.array(ans).shape[0]:
    print("")
    print(" convert from POSCAR to suggest.in :: SUCCESS")
    print(" # of atoms ::                    : %s" % counter2)
    print("")
  #
  return 0




if __name__ == '__main__':
  #
  print("*****************************************************************")
  print("    vasp_to_suggest.py --  Generator of ALM input file           ")
  print("                      Version. 1.0.0                             ")
  print("*****************************************************************")
  print("")
  #
  args = parser.parse_args()    # 4. 引数を解析
  VASP_input=args.arg1
  ALM_output=args.arg2
  # ====================
  #
  print(" Input File                     : %s" % VASP_input)
  print(" Output File                    : %s" % ALM_output)
  print("")
  #
  read_write(VASP_input, ALM_output)
