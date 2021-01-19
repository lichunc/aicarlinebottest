from __future__ import unicode_literals
import os
import json
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

import configparser

import random

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message (event):
    text = event.message.text
    if text == "車輛辨識":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請上傳照片")
            )

    elif text == "查詢車輛資料":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請輸入車輛型號")
            )

    elif text == "維修保養廠推薦":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請輸入廠牌名稱")
            )

    elif text == "toyota_altis":
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://autos.yahoo.com.tw/p/r/w1200/car-trim/March2019/5433211bbfe874461faba74d5989ad97.jpeg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://linecorp.com/', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Toyota ALTIS', weight='bold', size='xl'),
                    # review
                    # BoxComponent(
                    #     layout='baseline',
                    #     margin='md',
                    #     contents=[
                    #         IconComponent(size='sm', url='https://example.com/gold_star.png'),
                    #         IconComponent(size='sm', url='https://example.com/grey_star.png'),
                    #         IconComponent(size='sm', url='https://example.com/gold_star.png'),
                    #         IconComponent(size='sm', url='https://example.com/gold_star.png'),
                    #         IconComponent(size='sm', url='https://example.com/grey_star.png'),
                    #         TextComponent(text='4.0', size='sm', color='#999999', margin='md',
                    #                       flex=0)
                    #     ]
                    # ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='資訊',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='資訊',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='價格',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="價格",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='更多資訊', uri='https://autos.yahoo.com.tw/new-cars/trim/toyota-corolla-altis%28new%29-2019-1.8%E5%B0%8A%E7%88%B5'),
                    ),
                    # # separator
                    # SeparatorComponent(),
                    # # websiteAction
                    # ButtonComponent(
                    #     style='link',
                    #     height='sm',
                    #     action=URIAction(label='WEBSITE', uri="https://example.com")
                    # )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="hello", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
        # elif :
        #         line_bot_api.reply_message(
        #             event.reply_token,
        #             TextSendMessage(text="辨識失敗")
        #             )
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message (event):
    if event.message.type=='image':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://autos.yahoo.com.tw/p/r/w1200/car-trim/March2019/5433211bbfe874461faba74d5989ad97.jpeg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://linecorp.com/', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Toyota ALTIS', weight='bold', size='xl'),
                    # review
                    # BoxComponent(
                    #     layout='baseline',
                    #     margin='md',
                    #     contents=[
                    #         IconComponent(size='sm', url='https://example.com/gold_star.png'),
                    #         IconComponent(size='sm', url='https://example.com/grey_star.png'),
                    #         IconComponent(size='sm', url='https://example.com/gold_star.png'),
                    #         IconComponent(size='sm', url='https://example.com/gold_star.png'),
                    #         IconComponent(size='sm', url='https://example.com/grey_star.png'),
                    #         TextComponent(text='4.0', size='sm', color='#999999', margin='md',
                    #                       flex=0)
                    #     ]
                    # ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='資訊',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='資訊',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='價格',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="價格",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='更多資訊', uri='https://autos.yahoo.com.tw/new-cars/trim/toyota-corolla-altis%28new%29-2019-1.8%E5%B0%8A%E7%88%B5'),
                    ),
                    # # separator
                    # SeparatorComponent(),
                    # # websiteAction
                    # ButtonComponent(
                    #     style='link',
                    #     height='sm',
                    #     action=URIAction(label='WEBSITE', uri="https://example.com")
                    # )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="car_information", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
#         bubble_string = """
#         {
#             "type": "bubble",
#             "hero": {
#                 "type": "image",
#                 "url": "https://autos.yahoo.com.tw/p/r/w1200/car-trim/March2019/5433211bbfe874461faba74d5989ad97.jpeg",
#                 "size": "full",
#                 "aspectRatio": "20:13",
#                 "aspectMode": "cover",
#                 "action": {
#                 "type": "uri",
#                 "uri": "http://linecorp.com/"
#                 }
#                 },
#                 "body": {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [
#                         {
#                             "type": "text",
#                             "text": "Toyota ALTIS",
#                             "weight": "bold",
#                             "size": "xl"
#                         },
#                         {
#                             "type": "box",
#                             "layout": "vertical",
#                             "margin": "lg",
#                             "spacing": "sm",
#                             "contents": [
#                                 {
#                                     "type": "box",
#                                     "layout": "baseline",
#                                     "spacing": "sm",
#                                     "contents": [
#                                     {
#                                         "type": "text",
#                                         "text": "資訊",
#                                         "color": "#aaaaaa",
#                                         "size": "sm",
#                                         "flex": 1
#                                     },
#                                     {
#                                         "type": "text",
#                                         "text": "資訊",
#                                         "wrap": true,
#                                         "color": "#666666",
#                                         "size": "sm",
#                                         "flex": 5
#                                     }
#                                 ]
#                             },
#                         {
#                             "type": "box",
#                             "layout": "baseline",
#                             "spacing": "sm",
#                             "contents": [
#                         {
#                             "type": "text",
#                             "text": "價格",
#                             "color": "#aaaaaa",
#                             "size": "sm",
#                             "flex": 1
#                         },
#                         {
#                             "type": "text",
#                             "text": "價格",
#                             "wrap": true,
#                             "color": "#666666",
#                             "size": "sm",
#                             "flex": 5
#                         }
#                     ]
#                 }
#             ]
#         }
#     ]
#   },
#   "footer": {
#     "type": "box",
#     "layout": "vertical",
#     "spacing": "sm",
#     "contents": [
#       {
#         "type": "button",
#         "style": "link",
#         "height": "sm",
#         "action": {
#           "type": "uri",
#           "label": "更多資訊",
#           "uri": "https://autos.yahoo.com.tw/new-cars/trim/toyota-corolla-altis%28new%29-2019-1.8%E5%B0%8A%E7%88%B5"
#         }
#       },
#       {
#         "type": "spacer",
#         "size": "sm"
#       }
#     ],
#     "flex": 0
#   }
# }
        # """
        # message = FlexSendMessage(alt_text="hello", contents=json.loads(bubble_string))
        # line_bot_api.reply_message(
        #     event.reply_token,
        #     message
        # )
    # elif:
    #         line_bot_api.reply_message(
    #             event.reply_token,
    #             TextSendMessage(text="辨識失敗")
    #             )

# # 學你說話
# @handler.add(MessageEvent, message=TextMessage)
# def pretty_echo(event):
    
#     # if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
#         # Phoebe 愛唱歌
#     pretty_note = '♫♪♬'
#     pretty_text = ''
    
#     for i in event.message.text:
    
#         pretty_text += i
#         pretty_text += random.choice(pretty_note)

#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=pretty_text)
#     )

if __name__ == "__main__":
    app.run()