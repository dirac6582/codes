#!/bin/bash


# installが終わった後の各種appの設定．



# iterm2 shell integration
curl -L https://iterm2.com/misc/install_shell_integration.sh | bash



# iterm2 setting file
# https://dev-yakuza.posstree.com/environment/configure-development-environment-on-mac-with-homebrew-and-shell-script/#iterm2
cp ./com.googlecode.iterm2.plist ${HOME}/Library/Application\ Support/iTerm2/DynamicProfiles/
