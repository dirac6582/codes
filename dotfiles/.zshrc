############################################
# ~/.zshrc
#
#
#
# the orginal file is in ${HOME}/works/codes/.zshrc
#
############################################




# in ~/.zshenv, executed `unsetopt GLOBAL_RCS` and ignored /etc/zshrc
[ -r /etc/zshrc ] && . /etc/zshrc



#環境変数

#2020/2/23 TERM
#"xterm"だとemacs+solarizedが上手く表示されるが，"xterm+256color"ではemacs+solarizedは上手くいかない
export TERM="xterm-256color"
#export TERM="xterm-24bit"

# 可能なtermの設定は/usr/share/terminfo/以下に入っている．
# https://stackoverflow.com/questions/12345675/screen-cannot-find-terminfo-entry-for-xterm-256color/16566036


#
fpath+=$HOME/.zsh/pure





####################################################
#
#lsコマンドの色について
#
####################################################


# デフォルト設定(別になくても良い)
#LS_COLORS="デフォルトの色設定(ご自由に)"
#export LS_COLORS

#read dircolors
#dircolors-solarizedを使うため，対応するファイルを読み込む．

#対応するファイルの場所
# 2021/10/30 mv dotfiles to works/codes
dircolorsPATH=${HOME}/works/codes/dotfiles/iterm2setting/dircolors-solarized/dircolors.ansi-modify-dark
#dircolorsPATH=~/dotfiles/iterm2setting/dircolors-solarized/dircolors.ansi-modify-dark
#dircolorsPATH=~/dotfiles/iterm2setting/dircolors-solarized/dircolors.256dark
#以下で読み込み
if [ -f  ${dircolorsPATH} ];then
    if type dircolors >/dev/null 2>&1;then
	eval $(dircolors ${dircolorsPATH} )
    elif type gdircolors >/dev/null 2>&1;then
	eval $(gdircolors ${dircolorsPATH} ) 
    fi
else
    echo error DO NOT exist ${dircolorsPATH}
fi





#####補完機能について
##https://gist.github.com/d-kuro/352498c993c51831b25963be62074afa
# 補完機能有効にする
autoload -U compinit
compinit -u

# 補完候補に色つける
autoload -U colors
colors
zstyle ':completion:*' list-colors "${LS_COLORS}"

# 単語の入力途中でもTab補完を有効化
setopt complete_in_word
# 補完候補をハイライト
zstyle ':completion:*:default' menu select=1
# キャッシュの利用による補完の高速化
zstyle ':completion::complete:*' use-cache true
# 大文字、小文字を区別せず補完する
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'
# 補完リストの表示間隔を狭くする
setopt list_packed

# コマンドの打ち間違いを指摘してくれる
setopt correct
SPROMPT="correct: $RED%R$DEFAULT -> $GREEN%r$DEFAULT ? [Yes/No/Abort/Edit] => "



##########cd拡張機能

# cdを使わずにディレクトリを移動できる
setopt auto_cd
# $ cd - でTabを押すと、ディレクトリの履歴が見れる
setopt auto_pushd








#change prompt to pure
#autoload -U promptinit; promptinit
#prompt pure


#source /Users/amanotomohito/Downloads/Menlo-for-Powerline-master/'Menlo for Powerline.ttf'

# Gitブランチ名を表示
# https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh
#source ~/.git-prompt.sh

# Gitブランチの状況を*+%で表示
GIT_PS1_SHOWDIRTYSTATE=true
GIT_PS1_SHOWUNTRACKEDFILES=true
GIT_PS1_SHOWSTASHSTATE=true
GIT_PS1_SHOWUPSTREAM=auto


# # 出力の後に改行を入れます
# function add_line {
#   if [[ -z "${PS1_NEWLINE_LOGIN}" ]]; then
#     PS1_NEWLINE_LOGIN=true
#   else
#     printf '\n'
#   fi
# }
# PROMPT_COMMAND='add_line'


#export PS1='\[\e[37;100m\] \# \[\e[90;47m\]\[\e[30;47m\] \W \[\e[37m\]$(__git_ps1 "\[\e[37;102m\] \[\e[30m\] %s \[\e[0;92m\]")\[\e[49m\]\[\e[m\] \$ '











####################################################
#
#promptの設定について
#
####################################################

#color変更のために必要らしい
#https://www.sirochro.com/note/terminal-zsh-prompt-customize/#i-4
autoload -Uz colors
colors

#   %n ユーザ名
#   %m ホスト名
#   %* 24時間表示の時間
 
#   %{%B%}...%{%b%}: 「...」を太字にする。
#   %K{red}...%{%k%}: 「...」を赤の背景色にする。
#   %{%F{cyan}%}...%{%f%}: 「...」をシアン色の文字にする。
#   %n: ユーザ名
#   %?: 最後に実行したコマンドの終了ステータス
#   %(x.true-text.false-text): xが真のときはtrue-textになり
#                              偽のときはfalse-textになる。

##promptには，左側に表示するPROMPTと，右側に表示するRPROMPTがある．



#promptの表示．改行も楽ちん
#https://qrunch.net/@rugamaga/entries/XcrcLjb2vb5EfEUn
 # PROMPT='
 # %K{230}%F{33} %n%f %F{64}at%f %F{61}%m %f%k%K{245}%F{230}%f %F{230}%~%f%k%F{245}%f   %# '

function prompt-make {
    echo "\n %K{33}%F{235} %n%f %F{125}at%f %F{254}%m %f%k%K{136}%F{33}%f %F{230}%~ %f%k%F{136}%f   %# "
    return
}

 PROMPT='`prompt-make`'

 

#https://suwaru.tokyo/1箇所コピペするだけでgitブランチ名を常に表示【-zshrc/
# git ブランチ名を色付きで表示させるメソッド
function rprompt-git-current-branch {
  local branch_name st branch_status
 
  if [ ! -e  ".git" ]; then
      # git 管理されていないディレクトリは何も返さない
      echo "%F{245}\ue0b2%f%K{245}%F{230} %* \uf017%f %k"
    return
  fi
  branch_name=`git rev-parse --abbrev-ref HEAD 2> /dev/null`
  st=`git status 2> /dev/null`
  if [[ -n `echo "$st" | grep "^nothing to"` ]]; then
    # 全て commit されてクリーンな状態
    branch_status="%F{64} \ue0a0 ${branch_name}"
  elif [[ -n `echo "$st" | grep "^Untracked files"` ]]; then
    # git 管理されていないファイルがある状態
    branch_status="%F{160} \ue0a0 ${branch_name} \uf059"
  elif [[ -n `echo "$st" | grep "^Changes not staged for commit"` ]]; then
    # git add されていないファイルがある状態
    branch_status="%F{160} \ue0a0 ${branch_name} \uf055"
  elif [[ -n `echo "$st" | grep "^Changes to be committed"` ]]; then
    # git commit されていないファイルがある状態
    branch_status="%F{136} \ue0a0 ${branch_name} \uf06a"
  elif [[ -n `echo "$st" | grep "^rebase in progress"` ]]; then
    # コンフリクトが起こった状態
    echo "%F{160} \ue0a0 \uf05a (no branch)"
    return
  else
    # 上記以外の状態の場合
    branch_status="%F{33} ${branch_name}"
  fi
  # ブランチ名を色付きで表示する
  # echo "%F{245}\ue0b2%f%K{245}\ue0a0 ${branch_name} ${branch_status} %F{230}\ue0b2%k%f%K{230} %* %k"
  echo "%F{230}\ue0b2%f%K{230} ${branch_status} %F{245}\ue0b2%k%f%K{245}%F{230} %* \uf017%f %k"
}




# プロンプトが表示されるたびにプロンプト文字列を評価、置換する
setopt prompt_subst
 
#https://qiita.com/YumaInaura/items/874d5be9cfdb3d0415f1
RPROMPT='`rprompt-git-current-branch`'


##これは最終兵器．powerlevel9k 最悪これを設定すればよし
##https://chaika.hatenablog.com/entry/2019/06/09/090000

# POWERLEVEL9K_MODE='nerdfont-complete'
# source ~/dotfiles/iterm2setting/powerlevel9k/powerlevel9k.zsh-theme

# # Theme settings
# POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(ssh dir vcs newline status)
# POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=()
# POWERLEVEL9K_PROMPT_ADD_NEWLINE=true




##alias

#2020/2/23 ls
#これはsolarized colorになるようにわざわざcoreutilsを入れている
#https://joppot.info/2013/12/24/265
#

#eval `/usr/local/opt/coreutils/libexec/gnubin/dircolors ~/.dircolors-solarized/dircolors.ansi-dark`

alias ls='/opt/local/bin/gls -F --color=auto'
alias lsa='/opt/local/bin/gls -Fa --color=auto'
alias lsl='/opt/local/bin/gls -l --color=auto'


##2020/2/23 awk to gawk
alias awk='/opt/local/bin/gawk'


##2021/11/14 sed to gsed
alias sed='/opt/local/bin/gsed'

#2020/2/23 emacs

#####以下の問題はmacのデフォルトターミナルでの問題．解決するまでは使わない
#これはsolarizedを使う上で結構重大な問題．TERMがxterm-256colorsだとsolarizedが上手く動かないので，応急処置として，emacsのみxtermで起動するようにする．
#ただしこれはM-x list-colors-display初め多くの所に影響を及ぼす．
#alias e='TERM=xterm emacs -nw'
######


#iterm2では，true colorを使用可能．これによってemacs 26以降でtrue color版を使える．
#https://fossies.org/linux/emacs/doc/misc/efaq.texi#Colors-on-a-TTY
#alias e='TERM="xterm-24bit" emacs -nw'


##emacs --daemonを使う場合のaliasの設
#2021/10/28 
#emacs-daemon+true colorに移行,こっちを使い始める．
#xterm-directでもokらしい．
alias ee='TERM=xterm-24bit emacsclient -t'



#20200515 wine（temporary）
# alias wine='~/src/wine/wine64'



##iterm2 shell integration用のコマンド
test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"





# --------------------------------------
# Google search from terminal
# --------------------------------------
#2019/5/25 https://qiita.com/YuukiWatanabe/items/d3a684edb77be3804aa9
#google 「検索ワード」でsafariで検索できるようになる．

google(){
    if [ $(echo $1 | egrep "^-[cfs]$") ]; then
        local opt="$1"
        shift
    fi
    local url="https://www.google.co.jp/search?q=${*// /+}"
    local app="/Applications"
        local s="${app}/Safari.app"
    local g="${app}/Google Chrome.app"
    local f="${app}/Firefox.app"
    case ${opt} in
	"-s")   open "${url}" -a "$s";;
        "-g")   open "${url}" -a "$g";;
        "-f")   open "${url}" -a "$f";;

        *)      open "${url}";;
    esac
}



# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/amanotomohito/opt/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/amanotomohito/opt/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/amanotomohito/opt/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/amanotomohito/opt/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


# 2021/10/20
# hub 
# auto completion for hub
fpath=(~/.zsh/completions $fpath) 
autoload -U compinit && compinit

eval "$(hub alias -s)"


#  https://www.pandanoir.info/entry/2018/08/03/193000
function estart() {
  if ! emacsclient -e 0 > /dev/null 2>&1; then
    ({
      cd
      emacs --daemon
      cd -
    } > /dev/null 2>&1 & )
  fi
}
estart # シェル起動時にEmacsデーモンも起動する

# emacsclient用の追加の設定
# https://www.emacswiki.org/emacs/EmacsClient#h5o-1

alias ekill="emacsclient -e '(kill-emacs)'"
#alias erestart="ekill && estart"
#alias e="emacsclient -nw -a ''"
#alias emacs="emacsclient -nw -a ''"
export EDITOR="TERM=TERM=xterm-24bit emacsclient -a ''"
export ALTERNATE_EDITOR=""


# z
# https://github.com/rupa/z
source ~/src/z/z.sh


# iterm2 badge
# https://www.rasukarusan.com/entry/2019/04/13/180443
function badge() {
    printf "\e]1337;SetBadgeFormat=%s\a"\
    $(echo -n "$1" | base64)
}

function ssh_local() {
    local ssh_config=~/.ssh/config
    local server=$(cat $ssh_config | grep "Host " | sed "s/Host //g" | fzf)
    if [ -z "$server" ]; then
        return
    fi
    badge $server
    ssh $server
}
