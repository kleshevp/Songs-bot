import discord
import time

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!song Тайна хозяйки старинных часов'):
        await message.channel.send(f'Тайна хозяйки старинных часов\nЗаказал: @{message.author}')
        await message.channel.send(f'Деревня укрылась средь жутких лесов,')
        time.sleep(4)
        await message.channel.send('Туда совершенно случайно попал')
        time.sleep(4)
        await message.channel.send('Один покупатель старинных часов,')
        time.sleep(4)
        await message.channel.send('Он их для музея повсюду искал.')
        time.sleep(4)
        await message.channel.send('Не мог он не удивиться')
        time.sleep(4)
        await message.channel.send('Хозяйке старого особняка')
        time.sleep(4)
        await message.channel.send('Красивая с виду девица –')
        time.sleep(4)
        await message.channel.send('Откуда в этой глуши она?!')
        time.sleep(4)
        await message.channel.send('Висели над камином старинные часы,')
        time.sleep(4)
        await message.channel.send('И стрелки замерли на них сто с лишним лет назад.')
        time.sleep(4)
        await message.channel.send('Девица не спускала с них свой очень странный взгляд,')
        time.sleep(4)
        await message.channel.send('Они давно стоят.')
        time.sleep(4)
        await message.channel.send('Но нет, неподкупна хозяйка была –')
        time.sleep(4)
        await message.channel.send('Часы отказалась она продавать.')
        time.sleep(4)
        await message.channel.send('И на ночь оставила гостя она,')
        time.sleep(4)
        await message.channel.send('Свою предложила мужчине кровать.')
        time.sleep(4)
        await message.channel.send('Но только она заснула,')
        time.sleep(4)
        await message.channel.send('Тихонько дверь притворив за собой,')
        time.sleep(4)
        await message.channel.send('В гостиную прошмыгнула')
        time.sleep(4)
        await message.channel.send('Фигура гостя во тьме ночной.')
        time.sleep(4)
        await message.channel.send('Висели над камином старинные часы')
        time.sleep(4)
        await message.channel.send('И стрелки замерли на них сто с лишним лет назад')
        time.sleep(4)
        await message.channel.send('И гость не отрывал от них свой любопытный взгляд')
        time.sleep(4)
        await message.channel.send('Они давно стоят.')
        time.sleep(4)
        await message.channel.send('Не сразу он в них неисправность нашел,')
        time.sleep(4)
        await message.channel.send('Лишь колокол в старых часах зазвонил –')
        time.sleep(4)
        await message.channel.send('Обратно он в спальню хозяйки пошел:')
        time.sleep(4)
        await message.channel.send('Мол, древнюю вещь ото сна пробудил!')
        time.sleep(4)
        await message.channel.send('В ответ она захрипела,')
        time.sleep(4)
        await message.channel.send('Был дикий ужас в ее глазах.')
        time.sleep(4)
        await message.channel.send('Часы звенели – она старела,')
        time.sleep(4)
        await message.channel.send('Пока не превратилась в прах.')
        time.sleep(4)
        await message.channel.send('Висели над камином старинные часы,')
        time.sleep(4)
        await message.channel.send('И стрелки замерли на них сто с лишним лет назад.')
        time.sleep(4)
        await message.channel.send('Девица не спускала с них свой очень странный взгляд,')
        time.sleep(4)
        await message.channel.send(
            'Они давно стоят.\n\nСпасибо за прослушивание!\nПо желанию вы можете поставить печеньку @banan890 и @kleshevp')
        with open('Король и Шут - Тайна хозяйки старинных часов.mp3', 'rb') as file:
            file_data = discord.File(file)
            await message.channel.send(file=file_data, content='Тайна хозяйки старинных часов')
    elif message.content.startswith('!song Танец злобного гения'):
        await message.channel.send(f'Танец злобного гения\nЗаказал: @{message.author}')
        await message.channel.send('Проныра, озорник, ')
        time.sleep(4)
        await message.channel.send('Любитель книг,')
        time.sleep(4)
        await message.channel.send('Ловкач, игрок,')
        time.sleep(4)
        await message.channel.send('Жизнь между строк. ')
        time.sleep(4)
        await message.channel.send('И потому ')
        time.sleep(4)
        await message.channel.send('Открыт ему ')
        time.sleep(4)
        await message.channel.send('Незримый путь ')
        time.sleep(4)
        await message.channel.send('В любую суть. ')
        time.sleep(4)
        await message.channel.send('Танец злобного гения ')
        time.sleep(4)
        await message.channel.send('На страницах произведения. ')
        time.sleep(4)
        await message.channel.send('Это — игра, без сомнения, ')
        time.sleep(4)
        await message.channel.send('Обреченный ждет поражение! ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лала-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лала-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай. ')
        time.sleep(4)
        await message.channel.send('Подсыпать в душу яд ')
        time.sleep(4)
        await message.channel.send('Всегда он рад. ')
        time.sleep(4)
        await message.channel.send('Всего за час ')
        time.sleep(4)
        await message.channel.send('Прочтет он вас. ')
        time.sleep(4)
        await message.channel.send('Он волен взять ')
        time.sleep(4)
        await message.channel.send('И поменять ')
        time.sleep(4)
        await message.channel.send('Строку и с ней ')
        time.sleep(4)
        await message.channel.send('Смысл темы всей. ')
        time.sleep(4)
        await message.channel.send('Танец злобного гения ')
        time.sleep(4)
        await message.channel.send('На страницах произведения. ')
        time.sleep(4)
        await message.channel.send('Это — игра, без сомнения, ')
        time.sleep(4)
        await message.channel.send('Обреченный ждет поражение! ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лала-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лала-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай. ')
        time.sleep(4)
        await message.channel.send('Открыт роман, ')
        time.sleep(4)
        await message.channel.send('Читатель пьян, ')
        time.sleep(4)
        await message.channel.send('Разлив вино — ')
        time.sleep(4)
        await message.channel.send('Шагнул в окно. ')
        time.sleep(4)
        await message.channel.send('Танец злобного гения ')
        time.sleep(4)
        await message.channel.send('На страницах произведения. ')
        time.sleep(4)
        await message.channel.send('Это — игра, без сомнения, ')
        time.sleep(4)
        await message.channel.send('Обреченный ждет поражение! ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лала-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лала-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай. ')
        time.sleep(4)
        await message.channel.send('Танец злобного гения ')
        time.sleep(4)
        await message.channel.send('На страницах произведения. ')
        time.sleep(4)
        await message.channel.send('Это — игра, без сомнения, ')
        time.sleep(4)
        await message.channel.send('Обреченный ждет поражение! ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лала-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лала-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай ')
        time.sleep(4)
        await message.channel.send('Лала-ла-ла-лай.\n\nСпасибо за прослушивание!\nПо желанию вы можете поставить печеньку @banan890 и @kleshevp')
        with open('Король и Шут - Танец злобного гения.mp3', 'rb') as file:
            file_data = discord.File(file)
            await message.channel.send(file=file_data, content='Танец злобного гения')
    elif message.content.startswith('!song Прыгну со скалы'):
        await message.channel.send(f'Прыгну со скалы\nЗаказал: @{message.author}')
        await message.channel.send('С головы сорвал ветер мой колпак,')
        time.sleep(4)
        await message.channel.send('Я хотел любви, но вышло всё не так,')
        time.sleep(4)
        await message.channel.send('Знаю я ничего в жизни не вернуть')
        time.sleep(4)
        await message.channel.send('И теперь у меня один лишь только путь.')
        time.sleep(4)
        await message.channel.send('Разбежавшись, прыгну со скалы,')
        time.sleep(4)
        await message.channel.send('Вот я был и вот меня не стало,')
        time.sleep(4)
        await message.channel.send('И когда об этом вдруг узнаешь ты,')
        time.sleep(4)
        await message.channel.send('Тогда поймешь, кого ты потеряла.')
        time.sleep(4)
        await message.channel.send('Быть таким, как все с детства не умел')
        time.sleep(4)
        await message.channel.send('Видимо такой в жизни мой удел,')
        time.sleep(4)
        await message.channel.send('А она, да что она? Вечно мне лгала')
        time.sleep(4)
        await message.channel.send('И меня никогда понять бы не смогла.')
        time.sleep(4)
        await message.channel.send('Разбежавшись, прыгну со скалы,')
        time.sleep(4)
        await message.channel.send('Вот я был и вот меня не стало,')
        time.sleep(4)
        await message.channel.send('И когда об этом вдруг узнаешь ты,')
        time.sleep(4)
        await message.channel.send('Тогда поймешь, кого ты потеряла.')
        time.sleep(4)
        await message.channel.send('Гордо скину плащ, в даль направлю взор,')
        time.sleep(4)
        await message.channel.send('Может она ждет? Вряд ли. Это вздор,')
        time.sleep(4)
        await message.channel.send('И издав дикий крик, камнем брошусь вниз')
        time.sleep(4)
        await message.channel.send('Это моей жизни заключительный каприз.')
        time.sleep(4)
        await message.channel.send('Разбежавшись, прыгну со скалы,')
        time.sleep(4)
        await message.channel.send('Вот я был и вот меня не стало,')
        time.sleep(4)
        await message.channel.send('И тогда себя возненавидишь ты,')
        time.sleep(4)
        await message.channel.send('Лишь осознав, кого ты потеряла.')
        time.sleep(4)
        await message.channel.send('Кого ты потеряла.')
        time.sleep(4)
        await message.channel.send('Кого ты потеряла.\n\nСпасибо за прослушивание!\nПо желанию вы можете поставить печеньку @banan890 и @kleshevp')
        with open('Король и Шут - Прыгну со скалы.mp3', 'rb') as file:
            file_data = discord.File(file)
            await message.channel.send(file=file_data, content='Прыгну со скалы')
    elif message.content.startswith('!song Лесник'):
        await message.channel.send(f'Лесник\nЗаказал: @{message.author}')
        await message.channel.send('Замученный дорогой, я выбился из сил,')
        time.sleep(4)
        await message.channel.send('И в доме лесника я ночлега попросил.')
        time.sleep(4)
        await message.channel.send('С улыбкой добродушной старик меня впустил,')
        time.sleep(4)
        await message.channel.send('И жестом дружелюбным на ужин пригласил.')
        time.sleep(4)
        await message.channel.send('Будь как дома путник, я ни в чем не откажу,')
        time.sleep(4)
        await message.channel.send('Я ни в чем не откажу, я ни в чем не откажу!')
        time.sleep(4)
        await message.channel.send('Множество историй, коль желаешь расскажу,')
        time.sleep(4)
        await message.channel.send('Коль желаешь расскажу, коль желаешь расскажу!')
        time.sleep(4)
        await message.channel.send('На улице темнело, сидел я за столом.')
        time.sleep(4)
        await message.channel.send('Лесник сидел напротив, болтал о том, о сем.')
        time.sleep(4)
        await message.channel.send('Что нет среди животных у старика врагов,')
        time.sleep(4)
        await message.channel.send('Что нравится ему подкармливать волков.')
        time.sleep(4)
        await message.channel.send('Будь как дома путник, я ни в чем не откажу,')
        time.sleep(4)
        await message.channel.send('Я ни в чем не откажу, я ни в чем не откажу!')
        time.sleep(4)
        await message.channel.send('Множество историй, коль желаешь расскажу,')
        time.sleep(4)
        await message.channel.send('Коль желаешь расскажу, коль желаешь расскажу!')
        time.sleep(4)
        await message.channel.send('И волки среди ночи завыли под окном.')
        time.sleep(4)
        await message.channel.send('Старик заулыбался и вдруг покинул дом.')
        time.sleep(4)
        await message.channel.send('Но вскоре возвратился с ружьем на перевес:')
        time.sleep(4)
        await message.channel.send('"Друзья хотят покушать, пойдем приятель в лес!"')
        time.sleep(4)
        await message.channel.send('Будь как дома путник, я ни в чем не откажу,')
        time.sleep(4)
        await message.channel.send('Я ни в чем не откажу, я ни в чем не откажу!')
        time.sleep(4)
        await message.channel.send('Множество историй, коль желаешь расскажу,')
        time.sleep(4)
        await message.channel.send('Коль желаешь расскажу, коль желаешь расскажу!\n\nСпасибо за прослушивание!\nПо желанию вы можете поставить печеньку @banan890 и @kleshevp')
        with open('Король и Шут - Лесник.mp3', 'rb') as file:
            file_data = discord.File(file)
            await message.channel.send(file=file_data, content='Лесник')
    elif message.content.startswith('!song Кукла колдуна'):
        await message.channel.send(f'Кукла колдуна\nЗаказал: @{message.author}')
        await message.channel.send('Темный, мрачный коридор,')
        time.sleep(4)
        await message.channel.send('Я на цыпочках, как вор,')
        time.sleep(4)
        await message.channel.send('Пробираюсь, чуть дыша,')
        time.sleep(4)
        await message.channel.send('Чтобы не спугнуть')
        time.sleep(4)
        await message.channel.send('Тех, кто спит уже давно,')
        time.sleep(4)
        await message.channel.send('Тех, кому не все равно,')
        time.sleep(4)
        await message.channel.send('В чью я комнату тайком')
        time.sleep(4)
        await message.channel.send('Желаю заглянуть,')
        time.sleep(4)
        await message.channel.send('Чтобы увидеть.')
        time.sleep(4)
        await message.channel.send('Как бессонница в час ночной')
        time.sleep(4)
        await message.channel.send('Меняет, нелюдимая, облик твой,')
        time.sleep(4)
        await message.channel.send('Чьих невольница ты идей?')
        time.sleep(4)
        await message.channel.send('Зачем тебе охотиться на людей?')
        time.sleep(4)
        await message.channel.send('Крестик на моей груди,')
        time.sleep(4)
        await message.channel.send('На него ты погляди')
        time.sleep(4)
        await message.channel.send('Что в тебе способен он')
        time.sleep(4)
        await message.channel.send('Резко изменить')
        time.sleep(4)
        await message.channel.send('Много книжек я читал,')
        time.sleep(4)
        await message.channel.send('Много фокусов видал')
        time.sleep(4)
        await message.channel.send('Свою тайну от меня не пытайся скрыть!')
        time.sleep(4)
        await message.channel.send('Я это видел!')
        time.sleep(4)
        await message.channel.send('Как бессонница в час ночной')
        time.sleep(4)
        await message.channel.send('Меняет, нелюдимая, облик твой,')
        time.sleep(4)
        await message.channel.send('Чьих невольница ты идей?')
        time.sleep(4)
        await message.channel.send('Зачем тебе охотиться на людей?')
        time.sleep(4)
        await message.channel.send('Очень жаль, что ты тогда мне поверить не смогла,')
        time.sleep(4)
        await message.channel.send('В то, что новый твой приятель не такой как все!')
        time.sleep(4)
        await message.channel.send('Ты осталась с ним вдвоем,')
        time.sleep(4)
        await message.channel.send('Не зная ничего о нем.')
        time.sleep(4)
        await message.channel.send('Что для всех опасен он, наплевать тебе')
        time.sleep(4)
        await message.channel.send('И ты попала!')
        time.sleep(4)
        await message.channel.send('К настоящему колдуну,')
        time.sleep(4)
        await message.channel.send('Он загубил таких как ты, не одну!')
        time.sleep(4)
        await message.channel.send('Словно куклой, в час ночной')
        time.sleep(4)
        await message.channel.send('Теперь он может управлять тобой!')
        time.sleep(4)
        await message.channel.send('Все происходит как в страшном сне.')
        time.sleep(4)
        await message.channel.send('И находиться здесь опасно мне! ')
        with open('Король и Шут - Кукла колдуна.mp3', 'rb') as file:
            file_data = discord.File(file)
            await message.channel.send(file=file_data, content='Кукла колдуна')


client.run('Токен')
