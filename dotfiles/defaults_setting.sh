#!/bin/zsh



##このスクリプトは，macのdefauls設定を色々カスタマイズするためのスクリプト

##参考文献
#https://qiita.com/k-kozaki/items/febd07a22faee1b4704f
#http://baqamore.hatenablog.com/entry/2013/07/31/222438
#https://qiita.com/djmonta/items/17531dde1e82d9786816



######screenshot保存先変更

#保存先ディレクトリ作成
#ファイル存在が-eで確認できるように，dir存在は-dで確認できる．
SCREENSHOT_DIR=$HOME/Documents/Screenshots
if [ ! -d ${SCREENSHOT_DIR} ]; then
    mkdir ${SCREENSHOT_DIR}
fi

#screenshot保存先変更
defaults write com.apple.screencapture location ${SCREENSHOT_DIR}




##########finder設定

#隠しファイルの表示
#https://support.borndigital.co.jp/hc/ja/articles/360005975154-Finderで隠しファイル-隠しフォルダの表示-非表示
defaults write com.apple.finder AppleShowAllFiles TRUE



