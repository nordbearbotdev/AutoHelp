import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Я родился!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler(content_types=['text'])
def handle_text(message):

# Тригеры
if message.text == "Module vk_bottle not found":
   bot.send_message(message.from_user.id, 'Напишите в консоли, pip install vk_bottle'
                    
if message.text == "Module rich not found":
   bot.send_message(message.from_user.id, 'Напишите в консоли, pip install rich'
                    
if message.text == "DEBUG:urllib3.connectionpool:Starting new HTTPS conection":
   bot.send_message(message.from_user.id, 'Данная ошибка обозначает что идет созданиие нового HTTPS подлючения, но если после этого ничего не происходит, проверьте валидность ваших аккаунтов в ботнете.'
                    
if message.text == "DEBUG | vk_bottle.polling,user_polling.get_event":
   bot.send_message(message.from_user.id, 'Если вы встретились с этим, то удалите ботнет и скачайте его новую версию. в ней были убраны логи от vk_bottle.'                    


#Если пользователь отправил слово/фразу, на которое(ую) нет ответа
else:
   bot.send_message(message.from_user.id, "Извините, я Вас не понимаю")

bot.polling()                    
