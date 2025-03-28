import telebot
import random
import requests

# Token del bot de Telegram
BOT_TOKEN = '7271934921:AAFyQ5MeaDu9P-B3lGID86YbEhwJLUW8APo'

# Lista de URLs de imágenes motivacionales
MOTIVATIONAL_IMAGES = [
    "https://raw.githubusercontent.com/leyco9271/QQQQ/main/1.jpeg",
    "https://raw.githubusercontent.com/leyco9271/QQQQ/main/2.jpeg", 
    "https://raw.githubusercontent.com/leyco9271/QQQQ/main/3.jpeg"
]

# Inicializar el bot
bot = telebot.TeleBot(BOT_TOKEN)

# Manejador del comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola Cinthia, este bot te enviara mensajes motivacionales para cada dia, para que realice esta operacion envia el comando /envio")

# Manejador del comando /envio
@bot.message_handler(commands=['envio'])
def send_motivational_image(message):
    try:
        # Seleccionar una imagen aleatoria
        imagen_url = random.choice(MOTIVATIONAL_IMAGES)
        
        # Descargar la imagen
        response = requests.get(imagen_url)
        
        # Verificar si la descarga fue exitosa
        if response.status_code == 200:
            # Enviar la imagen
            bot.send_photo(message.chat.id, response.content)
        else:
            bot.reply_to(message, "Hubo un problema al descargar la imagen. Intenta de nuevo más tarde.")
    
    except Exception as e:
        bot.reply_to(message, f"Ocurrió un error: {str(e)}")

# Iniciar el bot
bot.polling()