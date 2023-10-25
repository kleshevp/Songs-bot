import discord
import requests
import time
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_message(message):
    # Проверка, чтобы бот не реагировал на свои собственные сообщения
    if message.author == bot.user:
        return

    # Обработка команды "/song"
    if message.content.startswith('/song'):
        # Разделение аргументов команды
        command_args = message.content.split(' ')
        if len(command_args) < 3:
            await message.channel.send('Неверная команда. Пример: /song автор песни название песни')
            return

        author = command_args[1]
        title = ' '.join(command_args[2:])

        # Определяем параметры для запроса к API Musixmatch
        api_key = 'musixmatch token'  # Вставьте ваш ключ API Musixmatch
        base_url = 'http://api.musixmatch.com/ws/1.1/'
        method = 'matcher.lyrics.get'
        params = {
            'apikey': api_key,
            'q_artist': author,
            'q_track': title,
        }

        response = requests.get(base_url + method, params=params)

        if response.status_code == 200:
            data = response.json()
            lyrics = data['message']['body']['lyrics']['lyrics_body']

            # Разделение строк текста песни
            lines = lyrics.split('\n')

            # Отправка каждой строки с задержкой в 4 секунды
            for line in lines:
                await message.channel.send(line)
                time.sleep(4)
        else:
            await message.channel.send('Песня не найдена.')

    await bot.process_commands(message)

bot.run('Discord token')
