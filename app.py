from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
