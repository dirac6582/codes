#!/bin/bash


#imageとしてはAが増えていくく変数，Cがそのmaxって感じ
A=0
C=40

#AがCより小さい間
while [ $A -le $C ]
do
    #出力するのはB，これを（今の場合1sごとに更新していく）
    B=""

    #seq a b c で，aからcまで，b間隔で数字を出力（今の場合bを省略）
    #その間に，$Bにどんどん-やspace，または>を追加していく
    for i in `seq 1 $C`
    do
	if [ $A -eq $i ]
	then
	    B="$B>"
	else
	    if [ $i -le $A ]
	    then
		B="$B-"
	    else
		B="$B "
	    fi
	fi
    done
    
    #%の表示
    P=`expr $A \* 100 / $C`

    # -e オプションでエスケープコードを有効に
    # -n オプションで改行を抑制
    # \r でカーソルを行頭に移動して、次の文字列を出力する
    #ただし，最終ステップ（A=C）では\rをやられると消えちゃうのでそれを阻止
    if [ $A -ne $C ];then
        echo -en " copying...  [$B] $P %\r"
    else
	echo  " copying...  [$B] $P % "
    fi
    

    #Aの更新．ここでは1s毎に更新しているが，本当はプログラム中にこのカウンターをいれる
    sleep 1
    A=`expr $A + 1`
done


  
