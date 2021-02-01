import requests
import config

token = config.TOKEN
chat_id = config.CHAT_ID

def telegram_bot_send_text(token,chat_id,message):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parser_mode=Markdown&text={message}'
    response = requests.get(url)
    return response.json()

def send_msn(text_msn):
    response = telegram_bot_send_text(token,chat_id,text_msn)
    print(response)

