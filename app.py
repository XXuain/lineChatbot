from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi(
    'Sran5QXp4EagW7p8t+WgTCUPqVZRZSp3hkdCba0B3PF5n8XdAc4BNLTp/znp1DIqEUNs07WME7bL9Rw0MPLXX3YQBLvHpmud05fx3l7fPHbAeh6pSq51lmumPkRkwZNqk+/nEisJf7/P5gXXIJir2QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('908635e70bf3b6c8abd64fad453b4465')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 使用者輸入的訊息
    reqMsg = event.message.text
    resMsg = ''
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=resMsg))

    if '來個圖圖' in reqMsg:
        resMsg = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

    if reqMsg in ['hi', 'Hi']:
        resMsg = '嗨嗨'

    line_bot_api.reply_message(event.reply_token, resMsg)


if __name__ == "__main__":
    app.run()
