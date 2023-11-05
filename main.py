import discord
import requests
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
is_started = {}

async def send_song(ctx, lines):
    for line in lines:
        if is_started[ctx]:
            line = line.strip()  # Удаляем начальные и конечные пробелы
            if line != "":  # Проверяем, что строка не является пустой
                    await ctx.send(line)
                    await asyncio.sleep(4)
            else:
                pass
        else:
            break

async def song(msg, channel, author, title):
    if not is_started[channel]:
        # Определяем параметры для запроса к API Musixmatch
        api_key = 'musixmatchAPI'
        base_url = 'http://api.musixmatch.com/ws/1.1/'
        method = 'matcher.lyrics.get'
        params = {
            'apikey': api_key,
            'q_artist': author,
            'q_track': title,
        }
        response = requests.get(base_url + method, params=params)
        
        if response.status_code == 200:
            is_started[channel] = True
            data = response.json()
            lyrics = data['message']['body']['lyrics']['lyrics_body']
            await channel.send(f'{author} - {title} заказал {msg.author.mention}')
            # Разделение строк текста песни
            lines = lyrics.split('\n')
            await send_song(channel, lines)
            is_started[channel] = False
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
        msg = message.content.split('/song ')[1]
        author, title = msg.split("-", 1)
        await song(message, message.channel, author, title)
    if message.content.startswith('/stop'):
        role_id = 1161221071308079134 or 1141065075533303918 or 1139273927290523728 or 1139998310652969140
        role = discord.utils.get(message.guild.roles, id=role_id)
        if role in message.author.roles:
            is_started[message.channel] = False
            await message.channel.send("Песня остановлена.")
    else:
        pass
@bot.command()
async def test(ctx):
    if not is_started[ctx]:
        await ctx.send('Бот работает и готов к использованию!')


bot.run('DiscordAPI')
