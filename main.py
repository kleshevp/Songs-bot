import discord
import requests
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
global is_started
is_started = False

async def song(msg, channel, author, title):
    global is_started
    if not is_started:
        # Определяем параметры для запроса к API Musixmatch
        api_key = 'musixmatch api'  # Вставьте ваш ключ API Musixmatch
        base_url = 'http://api.musixmatch.com/ws/1.1/'
        method = 'matcher.lyrics.get'
        params = {
            'apikey': api_key,
            'q_artist': author,
            'q_track': title,
        }
        response = requests.get(base_url + method, params=params)
        
        if response.status_code == 200:
            is_started = True
            data = response.json()
            lyrics = data['message']['body']['lyrics']['lyrics_body']
            await channel.send(f'{author} - {title} заказал {msg.author.mention}')
            # Разделение строк текста песни
            lines = lyrics.split('\n')
            # Отправка каждой непустой строки с задержкой в 4 секунды
            for line in lines:
                line = line.strip()  # Удаляем начальные и конечные пробелы
                if line != "":  # Проверяем, что строка не является пустой
                    if is_started:
                        await channel.send(line)
                        await asyncio.sleep(4)
                    else:
                        pass
                else:
                    pass
            is_started = False
        else:
            await channel.send('Песня не найдена.')
    else:
        pass
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('/song'):
        msg = message.content.split('/song ')[1]  # Получаем название песни из сообщения
        author, title = msg.split("-", 1)
        await song(message, message.channel, author, title)
@bot.command()
async def test(ctx):
    await ctx.send('Бот работает и готов к использованию!')



bot.run('Discord bot api')
