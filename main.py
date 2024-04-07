import os
import telebot
import webbrowser
import random
from rembg import remove
from PIL import Image
from telebot import types
from conf import TOKEN
from count_manager import load_processing_count, save_processing_count

processing_count = load_processing_count()
print("Processing count:", processing_count) 
print("Processing count loaded:", load_processing_count) 

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def greeting(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('/start')
    button2 = types.KeyboardButton('/help')
    button3 = types.KeyboardButton('/button')
    markup.row(button1, button2)
    markup.row(button3)
    file = open('./img/programmator.jpeg', 'rb')
    bot.send_photo(message.chat.id, file, 'Welcome to our Telegram Bot <b>RemoveBg</b>. All command are available in the menu', reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')
    bot.reply_to(message, '/start - Начать пользоваться ботом \n /help - Получить помощь')

@bot.message_handler(commands=['website', 'site'])
def website(message):
    webbrowser.open('https://unsplash.com')

@bot.message_handler(commands=['button'])
def get_buttonns(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Just a simple function!')
    markup.add(button)
    bot.send_message(message.chat.id, 'Command', reply_markup=markup)

@bot.message_handler(commands=['removebg'])
def get_removedbg(message):
    bot.send_message(message.chat.id, 'Send a clear picture to remove the background of your image')

    
    
@bot.message_handler(content_types=['photo', 'text'])
def on_removebg(message):
    print("Received a message of content type:", message.content_type)
    
    if message.content_type != 'photo':
        print("Received a message of content type:", message.content_type)
        bot.send_message(message.chat.id, 'Please send an image')

    # elif message.content_type == 'document':
    #     print("Received document message:", message.document)
    #     bot.send_message(message.chat.id, "Please send a photo, not a document!")

        if message.text == 'Send a clear picture to remove the background of your image':
            bot.reply_to(message, "Please send a photo to remove its background.")
            bot.send_message(message.chat.id, "Type a name for your image in document file:")
            
    elif message.content_type == 'photo':
        global processing_count
        wait_messages = [
            "Please wait while we process your request...",
            "We're working on it! Please be patient...",
            "Processing your request, this may take a moment...",
            "Hang tight! We're processing your request..."
        ]

        random_messages = random.choice(wait_messages)

        bot.send_message(message.chat.id, random_messages)
        input_photo = message.photo[-1].file_id
        file_info = bot.get_file(input_photo)
        downloaded_file = bot.download_file(file_info.file_path)

        input_path = os.path.join('media', 'inputs', f'input_{processing_count}.jpg')
        with open(input_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        input_image = Image.open(input_path)
        output_image = remove(input_image)

        output_path = os.path.join('media', 'outputs', f'output_{processing_count}.png')
        output_image.save(output_path)

        with open(output_path, 'rb') as document:
            bot.send_document(message.chat.id, document, caption="Here's a png format of your photo")


@bot.message_handler(content_types='text')
def get_hello(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hi, Im <b>Rayona</b>', parse_mode='html')
        # bot.reply_to(message, f'Hi, <b>{message.from_user.first_name}</b>!', parse_mode='html')
    elif message.text.lower() == 'give the code!':
        bot.reply_to(message, "print('Hello World')")
        bot.send_message(message.chat.id, "She is Saidislam's sister", parse_mode='html')
    elif message.text.lower() == 'provide me all the books':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.infinity_polling()