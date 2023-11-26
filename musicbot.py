import disnake
from disnake import Embed
import asyncio
from disnake.ext import commands
import json
import requests
from bs4 import BeautifulSoup as Soup
import re


def search_data(query: str):
    """
    Returns song data or raises FileNotFound error
    res = {
        'author': author,
        'title': song title,
        'image_url': url to image,
        'lyrics_path': url for lyrics page
    }
    """
    query = query.replace('  ', ' ').replace(' ', '+').replace('&', '%26').replace('-', '')
    url = f"https://genius.com/api/search/multi?q={query}"
    try:
        data = requests.get(url).json()
    except:
        raise ConnectionError
    if data['meta']['status'] != 200:
        raise FileNotFoundError
    else:
        try:
            song = data['response']['sections'][0]['hits'][0]['result']
        except:
            raise FileNotFoundError
        res = {
            'author': song['artist_names'],
            'title': song['title'],
            'image_url': song['header_image_url'],
            'lyrics_path': song['url']
        }
        return res


def clean_lyrics(s: str) -> str:
    while '\n\n' in s:
        s = s.replace('\n\n', '\n')
    s = s.replace('\n \n', '\n')
    s = s.replace('\n  \n', '\n')
    s = s.replace('\n ', '\n')
    while '\n\n' in s:
        s = s.replace('\n\n', '\n')
    return s


def get_lyrics(path: str) -> str:
    """
    Takes url as path to lyrics
    Returns str of song lyrics
    """
    data = requests.get(path).text
    soup = Soup(data, 'lxml')
    soup = soup.find('div', {'id': 'lyrics-root'})
    lyrics = ''
    for part in soup.find_all('div', {'class': re.compile('^Lyrics__Container')}):
        lyrics += Soup(part.prettify(), 'lxml').text
    return clean_lyrics(lyrics)


def search(query: str):
    """
    Takes string query that contains song name and author
    Return dictionary with results
    Example of return data:
    {
        'author': author,
        'title': song title,
        'image_url': url to image,
        'lyrics_path': url for lyrics page
        'lyrics': song lyrics
    }
    """
    s_data = search_data(query)
    s_data['lyrics'] = get_lyrics(s_data['lyrics_path'])
    return s_data



intents = disnake.Intents.default()
intents.members = True
intents.message_content = True
intents.typing = True
is_started = {}

command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

# Инициализация глобальных переменных
token = None
names1 = None
deny_list = None

with open('config.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
    text = json.load(f)  # загнали все, что получилось в переменную
    token = text['token']
    namesl = text['activity_name']

with open('deny_list.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
    text = json.load(f)  # загнали все, что получилось в переменную
    deny_list = text['deny_list']



activity = disnake.Activity(
    name=namesl,
    type=disnake.ActivityType.watching,
)

bot = commands.InteractionBot(intents=intents, command_sync_flags=command_sync_flags, activity=activity)


async def send_song(ctx, lines):
    for line in lines:
        if ctx.id in is_started and is_started[ctx.id]:
            line = line.strip()  # Удаляем начальные и конечные пробелы
            if line != "":  # Проверяем, что строка не является пустой
                await ctx.send(line)
                await asyncio.sleep(2.5)
            else:
                pass
        else:
            break
    is_started[ctx.id] = False


async def song_exe(msg, channel, author, title):
    if channel.id in is_started and not is_started[channel.id] or channel.id not in is_started:
        try:
            song_data = search(author+" "+title)
        except Exception as ex:
            await channel.send(f'Песня не найдена. 111 {ex}')
            is_started[channel.id] = False
        else:
            await channel.send(f'{song_data["author"]} - {song_data["title"]} заказал(-а) {msg.author.mention}')
            lines = song_data['lyrics'].split('\n')
            is_started[channel.id] = True
            await send_song(channel, lines)
            await channel.send(
                embed=Embed(
                description="Не забудьте отблагодарить banan890, Павел, Grisharik, yanesytortik печеньками",
                color=disnake.Color.gold()
                )
            )
            is_started[channel.id] = False
    else:
        pass



@bot.slash_command(description='Написать текст песни')
async def song(ctx, author: str, title: str):
    if ctx.author.id in deny_list:
        await ctx.response.send_message("Ты не достоин пользоваться этим ботом!")
    else:
        await ctx.response.send_message("Начинаю поиск песни")
        await asyncio.sleep(2)
        await song_exe(ctx, ctx.channel, author, title)


@bot.slash_command(description='Остановить музыку')
async def stop_song(ctx):
    if commands.has_permissions(mute_members=True):
        is_started[ctx.channel.id] = False
        await ctx.response.send_message("Песня остановлена.")
    else:
        await ctx.response.send_message("У вас нету разрешения")

@bot.slash_command(description='Add ID to deny list')
async def deny(ctx, option: str, id: str):
    if ctx.author.id == 994578923121807370:
        sid = int(id)
        with open('deny_list.json', 'r') as file:
            data = json.load(file)

        if option == 'add':
            data["deny_list"].append(sid)
            with open('deny_list.json', 'w') as file:
                json.dump(data, file)
            deny_list.append(sid)
            await ctx.response.send_message(f"Хозяин, {id} добавлен в запретный лист!")
        elif option == 'remove':
            data["deny_list"].remove(sid)
            with open('deny_list.json', 'w') as file:
                json.dump(data, file)
            deny_list.remove(sid)
            await ctx.response.send_message(f"Хозяин, {id} убран из запретного листа!")
        else:
            await ctx.response.send_message(f"Хозяин, вы указали неправильную опцию, пример: `/deny add/deny/get 123`!")


    else:
        await ctx.response.send_message("Минутку!\nВы не хозяин! Я отказываюсь выполнять!")




@bot.slash_command(description='Информация')
async def info_song(ctx):
        if ctx.channel.id in is_started and is_started[
            ctx.channel.id] == False or ctx.channel.id not in is_started:
            await ctx.response.send_message(
                "GitHub: https://github.com/kleshevp/Songs-bot 🤖\nCommunication with developers (Discord):\n@kleshevp - Программист(логика программы) 🧑‍💻\n@banan890#8186 - менеджер проекта 🍌\n@nikki0451 - Программист(логика программы) 👨‍💻\n@grisharik - /команды\n@yanesytortik - API и много чего ещё\n\nTry my commands:\n/song `Author's name` `song name`\n/info_song\n/stop {Stops the song/For server staff only}")
        else:
            pass

@bot.event
async def on_ready():
    print(f"Bot is ready {disnake.User}!")

bot.run(token)