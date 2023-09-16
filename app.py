import telebot

from config import keys
from config_token import TOKEN
from extensions import APIException, CryptoConvertor

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def start(message: telebot.types.Message):
    text  = 'Please enter: <currency> <target currency> <amount>\n\
for example USD BTC 100\ninfo about avaliable currencys please type /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text  = 'Please enter: <currency> <target currency> <amount>\n\n\
for example USD BTC 100\n\n'
    for key,value in keys.items():
        text += f'{value} = {key}\n'
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try: 
        value_check = message.text.split(' ')

        if len(value_check) != 3: raise APIException(f'To many items')
        
        quote,base,amount = value_check
        total = CryptoConvertor.get_price(quote,base,amount)

    except APIException as ex:
        bot.reply_to(message, f'Error in user input: {ex}')

    except Exception as ex:
        bot.reply_to(message, f'Error in program: {ex}')

    else:
        bot.reply_to(message, f'{amount} {quote} = {total} {base}')

bot.polling()