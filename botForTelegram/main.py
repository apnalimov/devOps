import telebot
import os
bot = telebot.TeleBot('6839103304:AAGVJ7RjeF7qJjqabzur3dZgZyVozfbTHSM')

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    deleteDjango = telebot.types.KeyboardButton(text="Удаление контейнера Django")
    createDjango = telebot.types.KeyboardButton(text="Создание контейнера Django")
    keyboard.add(deleteDjango, createDjango)
    deleteFastapi = telebot.types.KeyboardButton(text="Удаление контейнера FastApi")
    createFastapi = telebot.types.KeyboardButton(text="Создание контейнера FastApi")
    keyboard.add(deleteFastapi, createFastapi)
    rebootServer = telebot.types.KeyboardButton(text="Перезагрузка сервера")
    cmdDockerPs = telebot.types.KeyboardButton(text="docker ps")
    keyboard.add(rebootServer, cmdDockerPs)
    cmdDockerImages = telebot.types.KeyboardButton(text="docker images")
    keyboard.add(cmdDockerImages)
    
    
    bot.send_message(chat_id, 'Вот что я умею 🤡 /start', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Удаление контейнера Django')
def deleteDjango(message):
    chat_id = message.chat.id
    os.system("""ansible-playbook playbook.yaml --tags "delete_django_container" -i inventory.ini""")
    bot.send_message(chat_id, 'Контейнер Django удаляется')

@bot.message_handler(func=lambda message: message.text == 'Создание контейнера Django')
def createDjango(message):
    chat_id = message.chat.id
    os.system("cd ..")
    os.system("cd ansible")
    os.system("""ansible-playbook playbook.yaml --tags "create_django_container" -i inventory.ini""")
    bot.send_message(chat_id, 'Контейнер Django создается.\nДля проверки сервиса перейдите на http://apnalimov.ru:8000')

# @bot.message_handler(func=lambda message: message.text == 'Удаление контейнера FastApi')
# def deleteFastapi(message):
#     chat_id = message.chat.id
#     os.system("reboot now")
#     bot.send_message(chat_id, 'Контейнер FastApi удаляется')
    
# @bot.message_handler(func=lambda message: message.text == 'Создание контейнера FastApi')
# def createFastapi(message):
#     chat_id = message.chat.id
#     os.system("reboot now")
#     bot.send_message(chat_id, 'Контейнер Django создается.\nДля проверки сервиса перейдите на http://apnalimov.ru:9000')
    
@bot.message_handler(func=lambda message: message.text == 'Перезагрузка сервера')
def rebootServer(message):
    chat_id = message.chat.id
    os.system("reboot now")
    bot.send_message(chat_id, 'Сервер будет перезагружен в течении трёх минут')
    
@bot.message_handler(func=lambda message: message.text == 'docker ps')
def cmdDockerPs(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f'{os.popen("docker ps").read()}')
    
@bot.message_handler(func=lambda message: message.text == 'docker images')
def cmdDockerImages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, {os.popen("docker images").read()})
    
    


bot.polling()
