#!/usr/bin/env bash

# 未定義な変数があったら途中で終了する
set -u

# 今のディレクトリ
# dotfilesディレクトリに移動する
BASEDIR=$(dirname $0)
cd $BASEDIR

# dotfilesディレクトリにある、ドットから始まり2文字以上の名前のファイルに対して
# dirに対してもlinkを貼ろうとするのでそれはやめさせる。
for f in .??*; do
    [ "$f" = ".git" ] && continue
    [ "$f" = ".gitignore" ] && continue
    [ "$f" = ".gitconfig.local.template" ] && continue
    [ "$f" = ".gitmodules" ] && continue
    [ "$f" = ".DS_Store" ] && continue
    [ "$f" = ".ssh" ] && continue
    [ "$f" = ".emacs.d" ] && continue

    # シンボリックリンクを貼る
    ln -snfv ${PWD}/"$f" ~/
done

# init.elのリンクをはる．
if [ ! -d ${HOME}/.emacs.d ];then
    mkdir ${HOME}/.emacs.d
fi
ln -snfv ${PWD}/.emacs.d/init.el ~/.emacs.d/init.el

# make directories for emacs
if [ ! -d ${HOME}/.emacs.d/elpa ];then
    mkdir ${HOME}/.emacs.d/elpa
fi
if [ ! -d ${HOME}/.emacs.d/elips ];then
    mkdir ${HOME}/.emacs.d/elips
fi
if [ ! -d ${HOME}/.emacs.d/conf ];then
    mkdir ${HOME}/.emacs.d/conf
fi
if [ ! -d ${HOME}/.emacs.d/public_repos ];then
    mkdir ${HOME}/.emacs.d/public_repos
fi
if [ ! -d ${HOME}/.emacs.d/site-lisp ];then
    mkdir ${HOME}/.emacs.d/site-lisp
fi

# sshのlinkをはる。
mkdir ${HOME}/.ssh
ln -snfv ${PWD}/.ssh/config ${HOME}/.ssh/config

# emacs true color用の設定．
# https://stackoverflow.com/questions/14672875/true-color-24-bit-in-terminal-emacs
tic -x -o ${HOME}/.terminfo ${BASEDIR}/.terminfo/78/terminfo-24bit.src
