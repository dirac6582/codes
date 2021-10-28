#!/bin/bash

############
#
#ssh-keygenを対話なく作ることのできるシェル
#
############



#########
#
#SET VARIABLES
#
#########

#variables for ssh-keygen
filename=$HOME/.ssh/id_rsa_github
password=

#variables for config
host=github github.com
hostname=github.com
user=git



#########
#
#MAIN
#
#########


#make keys
ssh-keygen -t rsa -f ${filename} -N ""


#ローカルのconfigファイルを設定する必要あり
#EOFはヒアドキュメントと呼ばれるもの
#>だと新規，>>で上書きなので注意
cat <<EOF >> ~/.ssh/config
Host ${host}
   Hostname ${hostname}
   User ${user}
   IdentityFile ${filename}

EOF


#pubをコピーする必要があるので，暫定的な処置としてcatでターミナル上に表示する
echo "${filename}.pub"
echo ""
cat ${filename}.pub



#END
