#!/bin/bash

##
#
# 2021/10/28 ver1
# mount ssh server to local
#
##

## ----------------------------
# do shell script "/usr/local/bin/sshfs ユーザ名@ホスト名:接続先のフォルダのパス マウントポイント用のパス -oIdentityFile=~/.ssh/id_rsa -p ポート番号"
#
# --ユーザ名：自分がそのサーバーにログインする時のユーザー名
# --ホスト名：接続したいホスト名
# --接続先のフォルダのパス：サーバーでの自分のホームフォルダにするといいと思います
# --マウントポイントのパス：自分が作ったマウントさせたいフォルダへのパス
# --ポート番号：プロバイダによっては接続してほしいポート番号が違っていたりするみたいです。プロバイダのマニュアル参照の事
## ----------------------------


#接続前にすでに繋がっていれば切断する．
# 接続解除

if [ ! -d ~/sauron ]; then
    # 存在しない場合は作成（本処理へ)
    diskutil unmount ~/sauron
fi



# sauronへの接続
#sshfs amano@sauron3:/home/amano ~/sauron -oIdentityFile ~/.ssh/id_sauron_imacnew -p 22

sshfs amano@sauron3:/home/amano ~/sauron -p 22



