#########################################
#
# dot files
#
#########################################

# 



## contents

1, shell setting
- .zshrc
- .zshenv
- .zprofile


2, git setting
- .gitconfig



3, auto installation for Homebrew




4, GUI apps installation


- notion
- keepassXC
- things
- VS code
- iterm
- zotero
- slack
- skim



5, setting not included

Due to security issue
- keepassXC key files
- ssh
- 




##シンボリックリンクを貼るときの相対パスの指定についての注意
#ln -s シンボリックリンクからのパス シンボリックリンクのパス が正しい
https://www.tweeeety.blog/entry/20121129/1354192716
#ただ，これだとわかりにくい．とりあえずdotfilesに関してだけ言えば，ホームディレクトリに$HOMEを用いて絶対パスで指定した方が良い．



##emacsのtrue color設定について
tic -x -o ~/.terminfo terminfo-24bit.src
を実行すること．

