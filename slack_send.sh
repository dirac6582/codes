#!/bin/sh


##2020/3/27 this is the shell script which send a message to slack.
#https://qiita.com/tt2004d/items/50d79d1569c0ace118d6

###使いかた
#echo test1 | ./slack_send.sh


set -eu

#Incoming WebHooksのURL
WEBHOOKURL="https://hooks.slack.com/services/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"


####メッセージを保存する一時ファイル（最終的にこれを使う）
#ここで注意があって，どうもLinuxとOSXでmktemp（ファイル名がよくわからないファイルを作るコマンド）の動き方が違う．
#以下はosxで有効な書き方
#MESSAGEFILE=$(mktemp -t webhooks)
#一方Linuxでは，Xと書いたところを置き換える仕組みになっていて，このXを3つ以上いれる必要がある．
MESSAGEFILE=$(mktemp -t XXX.webhooks)
trap "
rm ${MESSAGEFILE}
" 0

usage_exit() {
    echo "Usage: $0 [-m message] [-c channel] [-i icon] [-n botname]" 1>&2
    exit 0
}

while getopts c:i:n:m: opts
do
    case $opts in
        c)
            CHANNEL=$OPTARG
            ;;
        i)
            FACEICON=$OPTARG
            ;;
        n)
            BOTNAME=$OPTARG
            ;;
        m)
            MESSAGE=$OPTARG"\n"
            ;;
        \?)
            usage_exit
            ;;
    esac
done


#slack 送信チャンネル
CHANNEL=${CHANNEL:-"#programs"}

#slack 送信名
BOTNAME=${BOTNAME:-"mybot"}

#slack アイコン
FACEICON=${FACEICON:-":ghost:"}

#見出しとなるようなメッセージ
MESSAGE=${MESSAGE:-""}


if [ -p /dev/stdin ] ; then
    #改行コードをslack用に変換
    cat - | tr '\n' '\\' | sed 's/\\/\\n/g'  > ${MESSAGEFILE}
else
    echo "nothing stdin"
    exit 1
fi

WEBMESSAGE='```'`cat ${MESSAGEFILE}`'```'

#Incoming WebHooks送信
curl -s -S -X POST --data-urlencode "payload={\"channel\": \"${CHANNEL}\", \"username\": \"${BOTNAME}\", \"icon_emoji\": \"${FACEICON}\", \"text\": \"${MESSAGE}${WEBMESSAGE}\" }" ${WEBHOOKURL} >/dev/null
