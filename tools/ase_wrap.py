#!/usr/bin/env python3

# ==============================

# ====================
# parserの設定

import argparse    # 1. argparseをインポート

parser = argparse.ArgumentParser(description='ase wrapper  ')    # 2. パーサを作る

# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument('--inp','-i', help='input file type', choices=['vasp', 'cif'], required=True) 
parser.add_argument('--out','-o', help='output file type', choices=['vasp', 'cif'], required=True )
parser.add_argument('input', help='input filename') 
parser.add_argument('output', help='output filename')
# parser.add_argument('-a', '--arg4')   # よく使う引数なら省略形があると使う時に便利



import sys

# usage
# cif2vasp.py [prefix]


if __name__ == '__main__':
  #
  print("*****************************************************************")
  print("    ase_wrap.py --  convert file types                           ")
  print("                      Version. 1.0.0                             ")
  print("*****************************************************************")
  print("")
  #
  args = parser.parse_args()    # 4. 引数を解析
  in_filetype  = args.inp
  out_filetype = args.out
  in_filename  = args.input
  out_filename = args.output

  # ====================
  #
  print(" Input File                     : %s" % in_filename)
  print(" Output File                    : %s" % out_filename)
  print("")
  #
  from ase import io
  atoms = io.read(in_filename)
  atoms.write(out_filename, format = out_filetype)

