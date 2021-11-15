#!/bin/bash


# cloning other repositories

# z.sh
git clone git://github.com/rupa/z ${HOME}/src/z/



## iterm2 font/color setting
#dircolors-solarized/
#solarized/
#Menlo-for-Powerline/ → homebrewへ変更
# nerd-fonts/ → homebrewでもinstallしているが，こっちでもやらないとだめかも．

git clone git@github.com:seebi/dircolors-solarized.git ${PWD}/iterm2setting/dircolors-solarized/
git clone git@github.com:altercation/solarized.git ${PWD}/iterm2setting/solarized/
# git clone git@github.com:abertsch/Menlo-for-Powerline.git ${PWD}/iterm2setting
git clone --depth 1  git@github.com:ryanoasis/nerd-fonts.git ${PWD}/iterm2setting 

