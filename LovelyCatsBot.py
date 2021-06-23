
import telebot
import random

def list_in_file(file_name,path_of_file = "./",encoding_file = "utf-8",split_symbol = '\n'):
       
       with open(file_name, mode="r",encoding=encoding_file) as file:
           array = []
           f = file.read()
               
           array = f.split(split_symbol)
           return array

stikers_ID = list_in_file("Stickers.txt") 
#ID стікерві, що може надсилати бот
emoji_ID = ['\U0001F638', '\U0001F639', '\U0001F63A', '\U0001F63B', '\U0001F63C',
            '\U0001F63D', '\U0001F63E', '\U0001F63F', '\U0001F640']
# код emoji у юнікод, що може надсилати бот    

bot = telebot.TeleBot('1878281166:AAHWvOJWIql1LFTGzZozAFsfkQ_Eu-09TIQ')

@bot.message_handler(commands=['start']) #реакція чат бота на стартову команду
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт! Я бот-котик:3')
    bot.send_message(message.chat.id, 'Я можу надсилати стікери та emoji котиків:3\nОберіть команду:\n/sticker\n/emoji')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Я можу надсилати стікери та emoji котиків:3\nОберіть команду:\n/sticker\n/emoji')
    
@bot.message_handler(commands=['sticker'])
def sticker(message):
    bot.send_sticker(message.chat.id,  random.choice(stikers_ID))
    
@bot.message_handler(commands=['emoji'])
def emoji(message):
    bot.send_message(message.chat.id,  random.choice(emoji_ID))
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привіт':
        bot.send_message(message.from_user.id, 'Привіт! Я бот-котик:3')
    elif message.text == 'привіт':
        bot.send_message(message.from_user.id, 'Привіт! Я бот-котик:3')
    elif message.text == 'Мяу':
        bot.send_message(message.from_user.id, 'Мур')
    elif message.text == 'Мур':
        bot.send_message(message.from_user.id, 'Мяу') 
    elif message.text == 'мяу':
        bot.send_message(message.from_user.id, 'Мур')
    elif message.text == 'мур':
        bot.send_message(message.from_user.id, 'Мяу')
    elif message.text == 'Пока':
        bot.send_message(message.from_user.id, 'Бувай. Гарного дня!')
    elif message.text == 'пока':
        bot.send_message(message.from_user.id, 'Бувай. Гарного дня!')
    else:
        bot.send_message(message.from_user.id, 'Не розумію\U0001F63F')

bot.polling(none_stop=True) # необхідно, щоб бот не вимкнувся відразу 

