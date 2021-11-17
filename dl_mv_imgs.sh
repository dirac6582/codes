#!/bin/bash
#https://stupiddog.jp/note/archives/1347

# usage
# ./mv.sh 拡張子 数 2021_01

# 引数の数の確認
if test $# -ne 3 ; then
    echo " # ERROR #"
    echo " # # of arguments is wrong #"
    echo " # ./mv.sh 拡張子 数 2021_01 "
    exit 1
fi
    
    

# 拡張子
end=$1

# number
max=`expr $2 + 1000`
echo ${max}

# output
output=$3

# 欲しい桁数＋１桁の数値を初期値に設定する
num=1
count=`expr ${num} + 1000`


# まずはdirを作成してファイルを移動．
mkdir ${output}
mv *.${end} ./${output}

# cd
cd ${output}

# 1から10まで
while [ ${count} -le ${max} ]
do
  # 変数展開で２文字目から末尾までを取得する(左１文字を捨てる）
    echo "${count:1}"
    echo ${count:1}.${end}
    echo ${num}.${end}
    mv ${num}.${end} ${count:1}.${end}
  # 算術展開でカウントアップ(カッコを使う方がinclementとしては早い)
  count=$((++count))
  num=$((++num))

done

# 最後に出力をまとめてpdfにする．
convert *.${end} output_${output}.pdf


