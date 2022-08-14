#!/usr/bin/env python3
#
# analyze.py
#


import argparse

description='''
       Simple script for plotting IFCs and Distances relations.
      Usage:
      $ python analyze.py file1.fcs

      For details of available options, please type
      $ python analyze.py -h
'''


parser = argparse.ArgumentParser(description=description)  
#
# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument("Filename"  , help='alamode *.fcs file')    # 必須の引数を追加
args = parser.parse_args()    # 4. 引数を解析



class Constant:
    '''
    physical constants
    '''
    ang_to_bohr=1.8897259886
    Ry_to_eV=13.605698066
    bohr_to_ang=0.529177249


# ==============
# こちらはfcsファイルからfcsの値と距離情報を読み込む.
# 

#クラス
class FcsDistance:
    '''
    This class stores a FCs value and the distance.
    '''
    def __init__(self,globalindex:int, fcs:float, distance:float):
        self.globalindex=globalindex
        self.fcs =fcs
        self.distance=distance


class FcsDistancePlot():
    def __init__(self,fcs_filename):
        self.__fcs_filename=fcs_filename # fcsファイル
        # self.maxorder=maxorder # maxorderを外部から入れる場合
        self.check_order= []
        self.maxorder= []
        self.localindex= []
        self.force_constant_with_distance= []
        self.__maxlength= []
        
    # fcsファイルのmaxorderを取得する．
    def get_order(self):
        import numpy as np
        self.check_order=np.zeros(5) # 2-6次があれば1，なければ0
        for i in range(6): #max6次までやってIFCsを調べる.
            # print("次数:: ", i+2)
            f = open(self.__fcs_filename, 'r')
            while True:
                data = f.readline()
                if data == "":
                    break
                if "*FC"+str(i+2) in data and "**FC"+str(i+2) not in data: 
                    self.check_order[i]=1
                    # print(data)
                    # check_orderの最大次数を取得
        self.maxorder=int(np.sum(self.check_order))
        print(" ----------------------------------")
        print(" maxorder is ::", self.maxorder+1)
        print("")
        #
        # fcsの数(local index)を取得する．
    def get_localindex(self):
        # fcs用のcounter
        self.localindex=[-1 for i in range(self.maxorder)]
        # 1回目の読み込みでlocal indexを読み込む
        # 時間はかかるが,次数ごとに一回読み込むようにした方が確実．
        for i in range(self.maxorder):
            # print("次数:: ", i)
            f = open(self.__fcs_filename, 'r')
            while True:
                data = f.readline()
                if self.localindex[i]>=0:
                    if data =="\n":
                        break
                    self.localindex[i]+= 1
                    #print(data)
                    #tmp=data.split()
                    # print(i, int(tmp[1]))
                    # *FC?を見つけたらカウントを開始
                if "*FC"+str(i+2) in data and "**FC"+str(i+2) not in data: 
                    self.localindex[i]=0
        print(" ----------------------------------")
        print(" local index for each order ::" , self.localindex)
        print("")

    # fcsの値と原子間距離を取得する．
    def get_fcs(self):
        # fcs用のcounter
        fcs_count=[-1 for i in range(self.maxorder)]
        # 出力するfcs
        self.force_constant_with_distance=[[] for y in range(self.maxorder)]
        # 読み込み
        for i in range(self.maxorder):
            # print("次数:: ", i)
            f = open(self.__fcs_filename, 'r')
            while True:
                data = f.readline()
                #            
                if fcs_count[i]>=0:
                    if data == "\n":
                        break
                    tmp=data.split()
                    self.force_constant_with_distance[i].append(FcsDistance(globalindex=int(tmp[0]),fcs=float(tmp[2]),distance=float(tmp[6+i])))
                    #
                    #  *FC?を見つけたらカウントを開始
                if "*FC"+str(i+2) in data and "**FC"+str(i+2) not in data: 
                    fcs_count[i]= 0
        print(" ----------------------------------")
        print(" finish loading fcs and distances ")
        print("")
    #
    # 得られたfcsをプロット
    def make_plots(self):
        import matplotlib.pyplot as plt
        import numpy as np
        # プロットを作成するにあたり，横軸は最も長い距離までに制限しておいた方が便利に思う．
        # とりあえずは2次IFCsの最大値を取得してこれを利用する．
        self.__maxlength=max(np.array([self.force_constant_with_distance[0][j].distance*Constant.bohr_to_ang for j in range(self.localindex[0]) ]))
        # print(self.__maxlength)
        # 
        for i in range(self.maxorder):
            fig, ax = plt.subplots(figsize=(8,5),tight_layout=True) 
            x = np.array([self.force_constant_with_distance[i][j].distance*Constant.bohr_to_ang for j in range(self.localindex[i]) ])
            y = np.array([self.force_constant_with_distance[i][j].fcs*Constant.Ry_to_eV/pow(Constant.bohr_to_ang,i+2) for j in range(self.localindex[i]) ])
            ax.set_xlim(0,self.__maxlength+2)
            ax.set_xlabel("distance "+r'$\AA$',fontsize=22)
            ax.set_ylabel("IFC[eV/"+r'$\AA$'+"^"+str(i+2)+"]",fontsize=22)
            ax.scatter(x,np.abs(y),label=str(i+2)+"th IFC")
            ax.legend(loc="upper right",fontsize=15 )
            # fig.show()
            fig.savefig(self.__fcs_filename+"."+str(i+2)+"th_order_ifc.pdf")
        print(" ----------------------------------")
        print(" finish making plots ")
        print("")
            
    # 全ての関数をまとめる．
    def process(self):
        self.get_order()
        self.get_localindex()
        self.get_fcs()
        self.make_plots()
        return 0


if __name__ == '__main__':
    '''
    Simple script for plotting IFCs and Distances relations.
    Usage:
    $ python analyze.py file1.fcs

    For details of available options, please type
    $ python analyze.py -h
    '''
    print("*****************************************************************")
    print("    analyze.py --  convert file types                           ")
    print("                      Version. 1.0.0                             ")
    print("*****************************************************************")
    print("")
     
    ARGS = parser.parse_args()    # 4. 引数を解析
    FCS_FILENAME = args.Filename

    if FCS_FILENAME == "":
        print("Usage: plotband.py [options] file1.bands file2.bands ...")
        print("For details of available options, please type\n$ python plotband.py -h")
        exit(1)
    PLOT=FcsDistancePlot(FCS_FILENAME)
    PLOT.process()
