#!/home/k0151/k015124/anaconda3/envs/ase/bin/python3
# #!/home/k0151/k015124/anaconda3/bin/python

##!/usr/bin/env python#
# plotrta.py
#
# Simple script to visualize Thermal conductivity from *.kl files.
#
#

import numpy as np
import matplotlib as mpl
from matplotlib.gridspec import GridSpec
#try:
#    mpl.use("Qt5agg")
#except:
#    pass
mpl.use('Pdf')
import matplotlib.pyplot as plt



import argparse    # 1. argparseをインポート
parser = argparse.ArgumentParser(description='ase wrapper  ')    # 2. パーサを作る
# 
# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument('arg1'  , help='alamode *.kl files',nargs='+')    # 必須の引数を追加
parser.add_argument('--tmin', help="minimum Temperature[K]", type=float, default="0.0")    # オプション引数（指定しなくても良い引数）を追加(type=で型指定)
parser.add_argument('--tmax', help="maximum Temperature[K]", type=float, default="-1")    # オプション引数（指定しなくても良い引数）を追加(type=で型指定)
parser.add_argument('-l', '--log', help="set logscale for xy axis", default="no" )
parser.add_argument('-a', '--axis', help="axis which is ploted. ", default="mean" )
#
#
args = parser.parse_args()    # 4. 引数を解析
#
# print('arg4='+args.arg4)




# font styles
mpl.rc('font', **{'family': 'Times New Roman', 'sans-serif': ['Helvetica']})
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=16)
mpl.rc('axes', labelsize=16)
mpl.rc('lines', linewidth=1.5)
mpl.rc('legend', fontsize='small')
# line colors and styles
color = ['b', 'g', 'r', 'm', 'k', 'c', 'y', 'r']
lsty = ['-', '-', '-', '-', '--', '--', '--', '--']


# ファイルからデータを読み込み
def read_files(filenames):
    # 格納するデータ
    datas=[]
    # 
    for i,name in enumerate(filenames):
        datas.append(np.loadtxt(name))
    return datas
    

# 指定されなかった場合のtmaxを決定する．
def decide_tmax(datas):
    maxlist=[]
    for i in range(len(datas)):
        maxlist.append(np.max(datas[i][:,0]))
    return np.max(maxlist)

# yのmaxminを取り出す．
def get_y_minmax(datas):

    ymin, ymax = [0, 0]

    for i in range(len(datas)):
        for j in range(len(datas[i])):
            for k in range(1, len(datas[i][j])):
                ytmp = datas[i][j][k]
                ymin = min(ymin, ytmp)
                ymax = max(ymax, ytmp)

    return ymin, ymax



# plotする
def run_plot(datas,tmin,tmax):
    # tmaxの指定
    if tmax==-1:
        print(" ")
        print(" WARNING : tmax is not specified. ")
        print("       Use maximum values in *.kl ")
        print(" ")
        tmax=decide_tmax(datas)

    # datasにある複数のデータをプロットする，
    fig, ax = plt.subplots()
    ax.set_xlim(tmin,tmax) # plot range[K]

    # これはなんだ？
    # gs = GridSpec(nrows=1, ncols=nax )
    # gs.update(wspace=0.1)
    # 
    # 複数データのプロット
    for i in range(len(datas)):
        # ax = plt.subplot(gs[iax])
        #
        if plot_axis == "mean":
            ax.plot(datas[i][:,0], (datas[i][:,1]+datas[i][:,5]+datas[i][:,9])/3,linestyle=lsty[i], color=color[i], label=filenames[i])

        # 
        # 初めのデータの時にcaptionをつける
        if i == 0:
            ax.set_ylabel("LTC (W/mK)", labelpad=20)
            ax.set_xlabel("Temp (K)", labelpad=20)
        else:
            ax.set_yticklabels([])
            ax.set_yticks([])

        # 
        # plt.axis([xmin_ax[iax], xmax_ax[iax], ymin, ymax])
        # ax.set_xticks(xticks_ax[iax])
        # ax.set_xticklabels(xticklabels_ax[iax])
        # ax.xaxis.grid(True, linestyle='-')

        #if options.print_key and iax == 0:
        #    ax.legend(loc='best', prop={'size': 10})
    ax.legend(loc='best', prop={'size': 10})
    plt.savefig("band.pdf")
    plt.show()



if __name__ == '__main__':
    '''
    Simple script for visualizing phonon dispersion relations.
    Usage:
    $ python plot_band.py [options] file1.bands file2.bands ...

    For details of available options, please type
    $ python plot_band.py -h
    '''
    #
    print("*****************************************************************")
    print("    ase_wrap.py --  convert file types                           ")
    print("                      Version. 1.0.0                             ")
    print("*****************************************************************")
    print("")
    #
    args = parser.parse_args()    # 4. 引数を解析
    filenames = args.arg1
    tmin = args.tmin
    tmax = args.tmax
    plot_axis = args.axis


    if len(filenames) == 0:
        print("Usage: plotband.py [options] file1.bands file2.bands ...")
        print("For details of available options, please type\n$ python plotband.py -h")
        exit(1)
    else:
        print(" ## ====")
        print(" Number of files = %d" % len(filenames))
        print(" ")
    #
    if plot_axis == "mean":
        print(" ## ====")
        print(" axis=mean :: We plot (k_xx+k_yy+k_zz)/3 " )
        print(" ")


    # read *.kl
    datas=read_files(filenames)
    #
    # decide tmax
    decide_tmax(datas)
    #
    # plot datas
    run_plot(datas,tmin,tmax)


    #nax, xticks_ax, xticklabels_ax, xmin_ax, xmax_ax, ymin, ymax, \
    #    data_merged_ax = preprocess_data(
    #        files, options.unitname, options.normalize_xaxis)

    #run_plot(nax, xticks_ax, xticklabels_ax,
    #         xmin_ax, xmax_ax, ymin, ymax, data_merged_ax)

