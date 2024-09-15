import telebot
import requests

bot = telebot.TeleBot("6874358355:AAHbTWIewyLnYru4IkRutj67OdDDaZ2qXV0")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f"Привет {message.from_user.first_name} {message.from_user.last_name}, рад тебя видеть")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, f"Сам ты {message.text}")

@bot.message_handler(content_types=['location'])
def handleLocation(message):
	lat = message.location.latitude
	lon = message.location.longitude
	res = requests.get(
		f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,rain,snowfall,cloud_cover&hourly=temperature_2m&forecast_days=1", )
	data = res.json()
	if message.content_type == "location":
		bot.reply_to(message, f"Погода сейчас: {data['current']['temperature_2m']}°С")

bot.infinity_polling()