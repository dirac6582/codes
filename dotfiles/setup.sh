#!/bin/zsh

######
##symbolic linksを作る．
##2020/3/18
##https://qiita.com/massy22/items/5bdb97f8d6e93517f916
######


###パス他
export DOTFILE_DIR=$HOME/dotfiles
export ITERM_DIR=$HOME/dotfiles/iterm2setting



###最初に設定するべき各種のディレクトリ等
function make_directories(){
    mkdir ${DOTFILE_DIR} 
    mkdir ${ITERM_DIR}
}



###DOT_FILESのシンボリックリンクを作る

function make_symbolic(){
    DOT_FILES=(.bashrc .bash_profile .zshrc .zshenv .zprofile .latexmkrc)
    
    for file in ${DOT_FILES[@]}
    do
	ln -s $HOME/dotfiles/$file $HOME/$file
    done
}







#Nerdfontのインストール
#https://vwrs.github.io/font/2018/09/26/nerd-fonts/
function nerd_fonts() {
  git clone --branch=master --depth 1 https://github.com/ryanoasis/nerd-fonts.git
  cd nerd-fonts
  ./install.sh $1  # "Source" to install Sauce Code Nerd Font
  cd ..
  rm -rf nerd-fonts
}



#solarizedテーマのダウンロード方法
function download_solarized(){
    #~/dotfiles/iterm2setting以下にcloneする．
    #https://hacknote.jp/archives/31390/
    if [ ! -e ${ITERM_DIR} ]; then
	mkdir ${ITERM_DIR}
    fi
    cd ${ITERM_DIR}
    git clone https://github.com/altercation/solarized.git
}





#スクリーンショットの保存先の変更
#https://book.mynavi.jp/macfan/detail_summary/id=90165
mkdir ~/ScreenShots/
defaults write com.apple.screencapture location ~/ScreenShots/;killall SystemUIServer
