#!/usr/bin/env bash

dotfiles_logo='
      | |     | |  / _(_) |           
    __| | ___ | |_| |_ _| | ___  ___  
   / _` |/ _ \| __|  _| | |/ _ \/ __| 
  | (_| | (_) | |_| | | | |  __/\__ \ 
   \__,_|\___/ \__|_| |_|_|\___||___/ 
  *** WHAT IS INSIDE? ***
  1. Download https://github.com/b4b4r07/dotfiles.git
  2. Symlinking dot files to your home directory
  3. Execute all sh files within `etc/init/` (optional)
  See the README for documentation.
'
echo "$dotfiles_logo"

# 未定義な変数があったら途中で終了する
set -u

# 今のディレクトリ
# dotfilesディレクトリに移動する
BASEDIR=$(dirname $0)
cd $BASEDIR

# dotfilesディレクトリにある、ドットから始まり2文字以上の名前のファイルに対して
# dirに対してもlinkを貼ろうとするのでそれはやめさせる。

echo 
echo "linking dot files ..."
echo
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
echo
echo "making directories for emacs..."
echo
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
