#!/usr/bin/env python3
#
# analyze_alm.py
#


import argparse
import sys
import numpy as np
import os

description='''
       Simple script for plotting IFCs and Distances relations/ ALM energy.
      Usage:
      $ python analyze_alm.py file1.fcs
      $ python analyze_alm.py file1.xml POSCAR1 POSCAR2 ...

      For details of available options, please type
      $ python analyze_alm.py -h
'''


parser = argparse.ArgumentParser(description=description)  
#
# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument("Filename"  , \
                    help='alamode *.fcs file or *.xml file.\n'
                    'analyze_alm.py automatically check the extention and decide what to do.') 

parser.add_argument("-O", "--OrigFile"  , \
                    help='VASP POSCAR files without displacement for calculation of energy')


parser.add_argument("-D", "--DispFile"  , \
                    nargs='+',
                    help='VASP POSCAR files with displacement for calculation of energy\n'
                    'multiple ')



args = parser.parse_args()    # 4. 引数を解析



class Constant:
    '''
    physical constants
    '''
    ang_to_bohr=1.8897259886
    Ry_to_eV=13.605698066
    bohr_to_ang=0.529177249



# 座標の差分を計算
# !! 注意 vaspはもともとAngstrom単位だが，ALAMODEに入れるのにbohr単位にする必要あり．
def calc_subtract(prim_filename,disp_filename):
    import ase.io
    import numpy as np
    
    # in angstrom
    primitive=ase.io.read(prim_filename).get_positions()
    displace=ase.io.read(disp_filename).get_positions()
    # ang to bohr
    subtract=(displace-primitive)*Constant.ang_to_bohr
    np.savetxt(disp_filename+".txt", subtract)
    return subtract

# *.txtファイルを入力すると一番大きいdisplacementを計算してくれる.
# これは実際にプロットを作る時に役に立つ.
def get_max_displace(filename):
    import numpy as np
    u0=np.loadtxt(filename)
    u_norm=np.linalg.norm(u0,axis=1)
    return np.amax(u_norm)

#クラス
class AtomCellSuper:
  def __init__(self,index:int, tran:int, cell_s:int):
    self.index=index
    self.tran =tran
    self.cell_s=cell_s

class FcsArrayWithCell:
  def __init__(self,fcs_val:float,pairs:AtomCellSuper):
    self.fcs_val=fcs_val
    self.pairs=pairs


# ======================
# rootを入力とする．
# load_system_info:全原子数,supercellの数,単位格子の原子数の取得
# make_mapping:map_p2s,map_s2pの読み込み

class System:
    def __init__(self,root):
        self.__root=root

    class Map: #s2p用
        def __init__(self,atom_num:int, tran_num:int):
            self.atom_num = atom_num
            self.tran_num = tran_num

    def load_system_info(self):
        # 全原子数
        self.__nat:int=int(self.__root.find("Structure").find("NumberOfAtoms").text)
        # supercellの数
        self.__ntran=int(self.__root.find("Symmetry").find("NumberOfTranslations").text)
        #単位格子の原子数
        self.__natmin = self.__nat // self.__ntran
        #結果出力
        print(" ============================")
        print(" nat (num of atoms in supercell)      = ",self.__nat)
        print(" ntran (num of symmetry operations)   = ",self.__ntran)
        print(" natmin(num of atoms in primitivecell = ",self.__natmin)
        print("")

        
    def make_mapping(self):
        import numpy as np
        self.map_p2s=np.zeros([self.__natmin,self.__ntran])
        self.map_s2p=[[] for i in range(self.__nat)]
        for child in self.__root.find("Symmetry").find("Translations"):
            tran   =int(child.get("tran"))-1  # 0スタートのために1引く
            atom_p =int(child.get("atom"))-1  
            atom_s =int(child.text)-1

            # primitive to super
            self.map_p2s[atom_p][tran] = atom_s
            # super to primitive
            self.map_s2p[atom_s]=self.Map(atom_num=atom_p,tran_num=tran)

    def __del__(self):
        del self.map_s2p
        del self.map_p2s
        del self.__nat
        del self.__ntran
        del self.__natmin
        del self.__root


class Fcs_phonon():
    def __init__(self,root,maxorder):
        self.__root=root # xmlファイル
        self.maxorder=maxorder
        # クラス間のやりとりについてはもう少しエレガントにできるはず.
        self.system=System(root=self.__root) #map_s2pを利用するので.
        self.system.load_system_info()
        self.system.make_mapping()
    
    def load_fcs_xml(self):
      from sympy.utilities.iterables import multiset_permutations
      # 出力するfcs
      self.force_constant_with_cell=[[] for y in range(self.maxorder)]
      # 次数のloop
      for order in range(self.maxorder):
        print(" reading order = ", order+2)
        if (order == 0):
          str_tag = "HARMONIC"
        else:
          str_tag = "ANHARM" + str(order + 2)
  
        # IFCsのloop
        for child in self.__root.find("ForceConstants").find(str_tag):
          # IFCを取得
          fcs_val:float=float(child.text) 

          # 初期化
          ivec_with_cell=[]
          ivec_tmp=[]
          ind=[] #permutation用.将来的には廃止

          # ======================
          # まずはpair1を取得
          tmp=[int(s) for s in child.get("pair1").split()]
          atmn:int =tmp[0]-1 #xmlは1スタート
          xyz:int  =tmp[1]-1
          ivec_with_cell.append(AtomCellSuper(index=3*self.system.map_p2s[atmn][0]+xyz,tran=0,cell_s=0)) #tran=0はdummy,pair1ではcel=0
          ivec_pair1=AtomCellSuper(index=3*atmn+xyz,tran=0,cell_s=0) #pair1のみここで追加
          # pair2以降
          for i in range(1,order+2):
            tmp=[int(s) for s in child.get("pair"+str(i+1)).split()]
            atmn:int   =tmp[0]-1
            xyz:int    =tmp[1]-1
            cell_s:int =tmp[2]-1
            ivec_with_cell.append(AtomCellSuper(index=3*atmn+xyz,tran=0,cell_s=cell_s)) #tran=0はdummy
            # ivec_tmp.append(AtomCellSuper(index=3*(map_s2p[atmn].atom_num - 1)+(xyz-1),tran=map_s2p[atmn].tran_num,cell_s=cell_s-1))
            ind.append(3*atmn+xyz)
          # ======================

          # ======================
          # permutation処理(次数だけのpairがある)
          # !! 現状cell_sの部分を同時に並び替えることができなかったので，代わりにpermutationの数を代入してある．
          # https://stackoverflow.com/questions/6284396/permutations-with-unique-values
          #for perm_list in multiset_permutations(ivec_with_cell[1:].index):
          #  for i in range(order+2-1):                #pair1を除いているので1引く
          #    atmn:int = int(perm_list[i].index / 3)  #3で割った商なので，atmnが出てくる.
          #    xyz:int  = perm_list[i].index % 3       #3でわった余なので，xyzが出てくる．
          #    ivec_tmp.append(AtomCellSuper(index=3*map_s2p[atmn].atom_num+xyz,tran=map_s2p[atmn].tran_num,cell_s=perm_list[i].cell_s))
          #
          #  force_constant_with_cell[order].append(FcsArrayWithCell(fcs_val=fcs_val,pairs=ivec_tmp))
          #
          multiplicity=len(list(multiset_permutations(ind)))

          for perm_list in multiset_permutations(ind):
            ivec_tmp=[ivec_pair1] #初期化
            # atmn_list= [ int(n /3) for n in perm_list]
            # xyz_list = [n % 3 for n in perm_list] 
            [ivec_tmp.append(AtomCellSuper(index=3*self.system.map_s2p[atmn].atom_num+xyz, tran=self.system.map_s2p[atmn].tran_num, cell_s=multiplicity)) for atmn,xyz in zip([ n//3 for n in perm_list], [n % 3 for n in perm_list])] 
            self.force_constant_with_cell[order].append(FcsArrayWithCell(fcs_val=fcs_val,pairs=ivec_tmp))
      #
      if not __debug__:
        for i in range(self.maxorder):
          print("  Number of non-zero IFCs for ", i + 2 , " order: (include permutation) ", len(self.force_constant_with_cell[i]))


    # calculate energy of only (i+2)-th order contribution.
    def calculate_energy_of_ith_order(self, u0, i:int):
      import math
      length:int   = len(self.force_constant_with_cell[i])   #その次数に入っているIFCsの数  
      nelem:int    = i + 2;                             #次数,つまりIFCsにnelemだけの原子が関わっている.
      factorial    = math.factorial(nelem)              #エネルギーのtaylor展開につける係数.
      U:float      = 0
      #
      for j in range(length):   #次数iでのIFCsの数に関するループ
        phi_val  = self.force_constant_with_cell[i][j].fcs_val
        dtmp     = 1.0/factorial * phi_val; #初期化 
        #
        for k in range(nelem): #IFCsでの原子に関するループ
          (atmn,xyz) = divmod(self.force_constant_with_cell[i][j].pairs[k].index, 3)   #3で割った商はatmn(in primitive cell).余はxyz.
          #
          dtmp   *=  u0[atmn][xyz]  
        U += dtmp
      # energy in eV unit.
      return U*Constant.Ry_to_eV

    # calculate_energy up to i-th order. frontend function.
    def calculate_energy(self, u0, i:int):
      if (i<2):
        print("error:: i should be 2 or more. i corresponds i-th order energy.")
      if (self.maxorder<i-1):
        print("error::maxorder is too small::maxorder should be i or more")
        return 1
      if i==2: # 2nd order
        return self.calculate_energy_of_ith_order(u0, i-2)
      else:
        return self.calculate_energy_of_ith_order(u0, i-2)+self.calculate_energy(u0, i-1)




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
       Simple script for plotting IFCs and Distances relations/ ALM energy.
      Usage:
      $ python analyze_alm.py file1.fcs
      $ python analyze_alm.py file1.xml POSCAR1 POSCAR2 ...

      For details of available options, please type
      $ python analyze_alm.py -h
    '''
    print("*****************************************************************")
    print("                      analyze_alm.py                             ")
    print("                      Version. 0.0.1                             ")
    print("*****************************************************************")
    print("")
     
    ARGS = parser.parse_args()    # 4. 引数を解析
    FCS_FILENAME = args.Filename

    if FCS_FILENAME == "":
        print("Error :: alm file(.fcs or .xml) is not specified ")
        print("For details of usage, please type\n$ analize_alm.py -h")
        exit(1)

        
    # if the file ends with .fcs, invoke FcsDistancePlot
    if ARGS.Filename.endswith(".fcs")== True:
        print(" ==========================")
        print(" invoke FcsDistantPlot :: making Distance vs FCs plots")
        print("")
        # warnings for --D and --A
        if ARGS.DispFile:
            print("")
            print(" WARNING :: Ignore DispFile")
            print("")
        if ARGS.OrigFile:
            print("")
            print(" WARNING :: Ignore OrigFile")
            print("")
        PLOT=FcsDistancePlot(FCS_FILENAME)
        PLOT.process()

    # if the file ends with .xml, invoke 
    if ARGS.Filename.endswith(".xml")== True:
        print(" ==========================")
        print(" invoke FcsPhonon :: calculate frozen phonon energies")
        print("")
        # warnings for --D and --A
        if ARGS.OrigFile:
            print("")
            print(" POSCAR with displacement     :: ", ARGS.OrigFile)
            print("")
        else:
            print("")
            print(" ERROR :: --OrigFile is needed for frozen phonon calculations")
            sys.exit(1)


        if ARGS.DispFile:
            print("")
            print(" POSCAR without displacement  :: ", ARGS.DispFile)
            print("")
        else:
            print("")
            print(" ERROR :: --DispFile is needed for frozen phonon calculations")
            sys.exit(1)

        # check if file exists
        if not os.path.isfile(ARGS.OrigFile):
            print("")
            print(" ERROR :: can not found :: ",ARGS.OrigFile)
        for dispname in ARGS.DispFile:
            if not os.path.isfile(dispname):
                print("")
                print(" ERROR :: can not found :: ",dispname)
                sys.exit(1)
            
            
        # XMLファイルを解析
        import xml.etree.ElementTree as ET 
        tree = ET.parse(ARGS.Filename) 
        # 一番上の階層の要素を取り出す.
        root = tree.getroot()

        # 系の情報をload
        fcs_phonon=Fcs_phonon(root=root,maxorder=5)

        # fcsを計算
        fcs_phonon.load_fcs_xml()
        print("# {:10} {:10} {:10} {:10} {:10} {:10}".format("u_norm[A]","E2[eV]","E3[eV]","E4[eV]","E5[eV]","E6[eV]"))            
        print("# ===================================")
        for dispname in ARGS.DispFile:
            calc_subtract(ARGS.OrigFile,dispname)
            u0=np.loadtxt(dispname+".txt")
            u_norm=get_max_displace(dispname+".txt")
            E2=fcs_phonon.calculate_energy(u0,2)
            E3=fcs_phonon.calculate_energy(u0,3)
            E4=fcs_phonon.calculate_energy(u0,4)
            E5=fcs_phonon.calculate_energy(u0,5)
            E6=fcs_phonon.calculate_energy(u0,6)
            # print(u_norm,E2,E3,E4,E5,E6)
            print("{:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}".format(u_norm,E2,E3,E4,E5,E6))
