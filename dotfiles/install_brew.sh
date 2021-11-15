#!/bin/bash

echo "installing homebrew..."
which brew >/dev/null 2>&1 || /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

echo "run brew doctor..."
which brew >/dev/null 2>&1 && brew doctor



# doctorの後にこれをやらないとupdate以降がうまく行かない．(MBP 2021 homeの設定で分かった．)
eval "$(/opt/homebrew/bin/brew shellenv)"


echo "run brew update..."
which brew >/dev/null 2>&1 && brew update

echo "ok. run brew upgrade..."
brew upgrade


echo "brew tap"
# brew tap thirdparty
# https://github.com/ryanoasis/nerd-fonts#option-4-homebrew-fonts 
brew tap homebrew/cask-fonts


echo "brew install..."
brew bundle --file=./brewfile




brew cleanup

echo "brew installed"
