#!/bin/bash

# 連番の作り方,ブレース展開
# https://qiita.com/laikuaut/items/642aa329a8d214a2cccb

cd result

for i in {0000..0020}
do
    echo $i
    # 他の0埋め方法
    # j=$(printf "%04d\n" "${i}")
    
    #copy files
    cp ../h2o_bec.ph.in ./${i}/WAT32_${i}.ph.in
    cp ../qe2.slurm ./${i}
done
