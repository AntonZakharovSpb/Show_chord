import pandas as pd
import telebot

sheet = pd.read_csv('chords_table.csv',index_col=0)
bot = telebot.TeleBot('bot_token') # Введите свой токен тут


menu = '''- Отправьте мне аккорд(латинскими буквами) и я скажу, как его зажимать(если аккорда пока нет в базе, я запомню, что вы спрашивали и добавлю его в ближайшее время)
 .
 - Связаться с разработчиком  напрямую: vk.com/id7189.
 .
 - p.s. Я ищу работу python developer junior или data analyst junior, открыт к предложениям - если они есть, напишите боту: резюме

'''

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, menu)
    
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        if message.text.lower()  == "меню" :
            bot.send_message(message.from_user.id, menu)
        elif message.text.lower() in sheet.index.values:
            bot.send_message(message.from_user.id, sheet.loc[message.text.lower()])
        elif message.text.lower() == 'резюме':
            bot.send_message(message.from_user.id, 'https://drive.google.com/file/d/1t50B4KPF4Q-2wXrBdXNXenXNzIKi_uR8/view?usp=sharing')
        else:
            bot.send_message(message.from_user.id, "Ваш запрос пока непонятен, и отправлен разработчику для улучшения работы Бота. Напишите мне Меню и я отвечу, что я могу")
            f = open(f'text1.txt', 'a')
            f.write('\n'+ message.text)
            f.close()

bot.polling()
