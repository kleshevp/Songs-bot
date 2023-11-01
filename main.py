import discord
import requests
import time
from discord.ext import commands
import genius

intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
global is_started
is_started = False

bot = commands.Bot(command_prefix='/', intents=intents)
@bot.command()
async def test(ctx):
    await ctx.send('Бот работает и готов к использованию!')

@bot.command()
async def song(ctx, msg):
    global is_started
    if not is_started:
        if "-" in msg:
            author, title = msg.split("-", 1)
            # Определяем параметры для запроса к API Musixmatch
            api_key = 'musixmatch API'  # Вставьте ваш ключ API Musixmatch
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
                await ctx.send(f'{author} {title} заказал {ctx.author.mention}')
                # Разделение строк текста песни
                lines = lyrics.split('\n')
                # Отправка каждой непустой строки с задержкой в 4 секунды
                for line in lines:
                    line = line.strip()  # Удаляем начальные и конечные пробелы
                    if line != "":  # Проверяем, что строка не является пустой
                        if is_started:
                            await ctx.send(line)
                            time.sleep(4)
                        else:
                            break
                    else:
                        pass
                is_started = False
            else:
                await ctx.send('Песня не найдена.')
        else:
            await ctx.send("Неправильный формат! Используйте: автор-название_песни")

bot.run('Discord API')
