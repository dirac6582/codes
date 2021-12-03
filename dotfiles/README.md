#########################################
#
# dot files
#
#########################################

# 


## 実際の設定
1, 事前準備
install xcode command line tools.

ssh connection to github

clone "codes" repository in ${HOME}/works


2, できること。


- clone.sh 他人の作ったgit repositoryをcloneする。
- ~/src/z.sh
- 


## contents

1, shell setting
- .zshrc
- .zshenv
- .zprofile


2, git setting
- .gitconfig
  .gitignore_global


3, emacs setting
- init.el



!! causion !!
before installation,
- xcode Tools
are needed.


3, auto installation for Homebrew

# apps
- mas
- anaconda3
- emacs

# commands
inetutils
imagemagick
sqlite


# gnu command replace
# https://qiita.com/eumesy/items/3bb39fc783c8d4863c5f
- coreutils --default-names (ls, mv)
- diffutils  (diff, cmp, diff3, sdiff)
- findutils (find, locate, updatedb, xargs)
- ed
- gawk
- gsed
- gnu-tar
- grep
- gzip

# テキスト処理
- ag
- jq
- lv
- parallel
- pandoc
- sift
- wget
- wdiff --with-gettext
- xmlstarlet



4, GUI apps installation for homebrew cask
https://qiita.com/takeshisakuma/items/e9685fb9e394212247c0

- alfread
- notion
- keepassXC
- things
- VS code
- iterm2
- zotero
- slack
- skim
- alfred
- deepl
- dropbox
- grammarly
- zoom
- chrome
- 

5, 


5, setting not included

Due to security issue
- keepassXC key files
- ssh key files
- 




##シンボリックリンクを貼るときの相対パスの指定についての注意
#ln -s シンボリックリンクからのパス シンボリックリンクのパス が正しい
https://www.tweeeety.blog/entry/20121129/1354192716
#ただ，これだとわかりにくい．とりあえずdotfilesに関してだけ言えば，ホームディレクトリに$HOMEを用いて絶対パスで指定した方が良い．



##emacsのtrue color設定について
tic -x -o ~/.terminfo terminfo-24bit.src
を実行すること．



6, TODO

２、色々echoで情報を出すようにしたい。

３、https://github.com/b4b4r07/dotfiles/blob/master/Makefile
を参考に、makeで自動的にやってくれるようにしたい。

５、やはりcodesとdotfileは分けておくべきでは？ という気がする。 今更どうしようもないのかもしれないけど。
→ 一応そういうわけでもないかもしれない。いずれにせよ一回試すべき。
→ というのも、わざわざgitにssh接続しなくて良いように、公開repositoryにしようと思うので。今使用しているdotfilesレポジトリがあるので、それを利用する形に変更したい。
→ これをやる場合、キーパスファイルやsshのファイルなどは同じrepositoryでは保管できなくなるので注意。
→ 後はsshkeygenのスクリプトも作って.sshディレクトリに入れておいた方が良い。

８、pdfpc：プレゼンテーションツール



9, python setting
https://mitsudo.net/python環境の構築-mac-with-anaconda-by-homebrew/

http://omilab.naist.jp/~mukaigawa/misc/Makefile.html
