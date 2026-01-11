import requests
import telebot

TOKEN = "8280323274:AAE27xDRJ-JB_I7miydOdhNul8-Tesr9rh0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help_command(message):
    bot.reply_to(message, 
        "Привет! Я бот погоды.\n"
        "Просто напиши мне 'погода'\n"
        "И я покажу погоду в Москве")

@bot.message_handler(func=lambda message: True)
def send_weather(message):
    text = message.text.lower()
    
    if "погод" in text:
        try:
            weather = requests.get("https://wttr.in/Moscow?format=3", timeout=5).text
            bot.reply_to(message, f"🌤 {weather}")
        except:
            bot.reply_to(message, "Попробуйте еще раз, сайт не отвечает :(")
    else:
        bot.reply_to(message, "Напиши 'погода'")

print("Бот запущен!")
bot.polling()
