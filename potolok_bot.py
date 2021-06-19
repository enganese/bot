import re
import sqlite3

import aiogram
import time
# from aiogram import *
from aiogram import types
from aiogram.utils import executor
import logging

logging.basicConfig(level=logging.INFO)

bot = aiogram.Bot('1877623989:AAEwRLoGjqYGno3I3NW8InLsYPVMdCW9s3E')
dp = aiogram.Dispatcher(bot)


@dp.callback_query_handler(lambda c: c.data == 'usluga')
async def abcabcabc(call):
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    multi_level = types.InlineKeyboardButton('Двухуровневые потолки', callback_data='multi')
    single_level = types.InlineKeyboardButton('Цветные потолки', callback_data='single')
    spaika_poloten = types.InlineKeyboardButton('Матовые потолки', callback_data='spaika')
    apply_level = types.InlineKeyboardButton('Резные потолки Apply', callback_data='apply')
    satinovye = types.InlineKeyboardButton('Сатиновые потолки', callback_data='satinovye')
    picture_on_potolok = types.InlineKeyboardButton('Потолки с фотопечатью',
                                                    callback_data='picture')
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_menu')
    markup2.add(multi_level, single_level, spaika_poloten, picture_on_potolok, apply_level, satinovye)
    markup2.row(n123)
    await bot.edit_message_text('У нас есть множество услуг, выберите подходящую вам!', call.message.chat.id,
                                call.message.message_id,
                                reply_markup=markup2)


# multi
@dp.callback_query_handler(lambda c: c.data == 'multi')
async def usluga(call):
    n2 = types.InlineKeyboardMarkup(row_width=1)
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_uslugi')
    example = types.InlineKeyboardButton('Посмотреть примеры', callback_data='multi_example')
    n2.row(example)
    n2.add(n123)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id, text='<b><i>Двухуровневые потолки</i></b>'
                                                                         '\n\nДвухуровневые натяжные потолки – это конструкции в несколько ярусов, '
                                                                         'где каждый уровень установлен на разной высоте. Такая технология установки'
                                                                         ' натяжных потолков помогает скрыть недостатки помещения, трубы, проводку. '
                                                                         'Но также это уникальное дизайнерское решение, которое достаточно необыкнов'
                                                                         'енно смотрится. Такой вариант позволяет сочетать матовые и глянцевые потол'
                                                                         'ки с подсветкой в одном помещении. Единственное ограничение для такого пол'
                                                                         'отка – его нельзя устанавливать в слишком низких помещениях.'
                                                                         '\n\n<b>Цена:</b> <u>2000 руб/м²</u>',
                                reply_markup=n2, parse_mode='html')


# multi example
@dp.callback_query_handler(lambda c: c.data == 'multi_example')
async def usluga(call):
    await types.ChatActions.upload_photo()
    media_multi = types.MediaGroup()
    media_multi.attach_photo('https://i.imgur.com/FMzi9AM.jpg')
    media_multi.attach_photo('https://i.imgur.com/xxc3tfc.jpg')
    media_multi.attach_photo('https://i.imgur.com/QfOWmlg.jpg', caption='<i>Пример - Двухуровневые потолки</i>',
                             parse_mode='html')
    await call.message.reply_media_group(media=media_multi)
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    multi_level = types.InlineKeyboardButton('Двухуровневые потолки', callback_data='multi')
    single_level = types.InlineKeyboardButton('Цветные потолки', callback_data='single')
    spaika_poloten = types.InlineKeyboardButton('Матовые потолки', callback_data='spaika')
    apply_level = types.InlineKeyboardButton('Резные потолки Apply', callback_data='apply')
    satinovye = types.InlineKeyboardButton('Сатиновые потолки', callback_data='satinovye')
    picture_on_potolok = types.InlineKeyboardButton('Потолки с фотопечатью',
                                                    callback_data='picture')
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_menu')
    markup2.add(multi_level, single_level, spaika_poloten, picture_on_potolok, apply_level, satinovye)
    markup2.row(n123)
    await call.message.answer(text='У нас есть множество услуг, выберите подходящую вам!',
                             reply_markup=markup2)


# satinovye potolky
@dp.callback_query_handler(lambda c: c.data == 'satinovye')
async def usluga(call):
    n2 = types.InlineKeyboardMarkup(row_width=1)
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_uslugi')
    example = types.InlineKeyboardButton('Посмотреть примеры', callback_data='satinovye_example')
    n2.row(example)
    n2.add(n123)
    await bot.edit_message_text(text='<b><i>Сатиновые потолки</i></b>'
                                     '\n\nСатиновые натяжные потолки пользуются заслуженной популярностью – обладая всеми достоинствами потолков ПВХ, они выглядят как дорогие тканевые. Сатиновые потолки красивы, удобны в использовании и отлично вписываются в любой интерьер.'
                                     '\n\n<b>Цена:</b> <u>450 руб/м²</u>',
                                reply_markup=n2, parse_mode='html', message_id=call.message.message_id, chat_id=call.message.chat.id)


# satinovye example
@dp.callback_query_handler(lambda c: c.data == 'satinovye_example')
async def usluga_apply(call):
    await types.ChatActions.upload_photo()
    media_multi = types.MediaGroup()
    media_multi.attach_photo('https://i.imgur.com/vFRdQGV.jpg')
    media_multi.attach_photo('https://i.imgur.com/N9AuY3O.jpg')
    media_multi.attach_photo('https://i.imgur.com/liBcq8r.jpg', caption='<i>Примеры - Сатиновые потолки</i>',
                             parse_mode='html')
    await call.message.reply_media_group(media=media_multi)
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    multi_level = types.InlineKeyboardButton('Двухуровневые потолки', callback_data='multi')
    single_level = types.InlineKeyboardButton('Цветные потолки', callback_data='single')
    spaika_poloten = types.InlineKeyboardButton('Матовые потолки', callback_data='spaika')
    apply_level = types.InlineKeyboardButton('Резные потолки Apply', callback_data='apply')
    satinovye = types.InlineKeyboardButton('Сатиновые потолки', callback_data='satinovye')
    picture_on_potolok = types.InlineKeyboardButton('Потолки с фотопечатью',
                                                    callback_data='picture')
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_menu')
    markup2.add(multi_level, single_level, spaika_poloten, picture_on_potolok, apply_level, satinovye)
    markup2.row(n123)
    await call.message.answer(text='У нас есть множество услуг, выберите подходящую вам!',
                              reply_markup=markup2)

# apply potolky
@dp.callback_query_handler(lambda c: c.data == 'apply')
async def usluga(call):
    n2 = types.InlineKeyboardMarkup(row_width=1)
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_uslugi')
    example = types.InlineKeyboardButton('Посмотреть примеры', callback_data='apply_example')
    n2.row(example)
    n2.add(n123)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='<b><i>Резные потолки Apply</i></b>'
                                     '\n\nРезные натяжные потолки представляют собой двухуровневые конструкции. '
                                     'В нижней поверхности выполняются художественные прорези, '
                                     'при накладывании которых на верхнее полотно образуется объемный рисунок.'
                                     '\n\n<b>Цена:</b> <u>1300 руб/м²</u>'
                                , reply_markup=n2, parse_mode='html')



# apply example
@dp.callback_query_handler(lambda c: c.data == 'apply_example')
async def usluga_apply(call):
    await types.ChatActions.upload_photo()
    media_multi = types.MediaGroup()
    media_multi.attach_photo('https://i.imgur.com/nrkVP8K.jpg')
    media_multi.attach_photo('https://i.imgur.com/3iwVxSf.jpg')
    media_multi.attach_photo('https://i.imgur.com/rS77w4Q.jpg', caption='<i>Примеры - Резные потолки Apply</i>',
                             parse_mode='html')
    await call.message.reply_media_group(media=media_multi)
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    multi_level = types.InlineKeyboardButton('Двухуровневые потолки', callback_data='multi')
    single_level = types.InlineKeyboardButton('Цветные потолки', callback_data='single')
    spaika_poloten = types.InlineKeyboardButton('Матовые потолки', callback_data='spaika')
    apply_level = types.InlineKeyboardButton('Резные потолки Apply', callback_data='apply')
    satinovye = types.InlineKeyboardButton('Сатиновые потолки', callback_data='satinovye')
    picture_on_potolok = types.InlineKeyboardButton('Потолки с фотопечатью',
                                                    callback_data='picture')
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_menu')
    markup2.add(multi_level, single_level, spaika_poloten, picture_on_potolok, apply_level, satinovye)
    markup2.row(n123)
    await call.message.answer(text='У нас есть множество услуг, выберите подходящую вам!',
                              reply_markup=markup2)


# single
@dp.callback_query_handler(lambda c: c.data == 'single')
async def usluga(call):
    n2 = types.InlineKeyboardMarkup(row_width=1)
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_uslugi')
    example = types.InlineKeyboardButton('Посмотреть примеры', callback_data='single_example')
    n2.row(example)
    n2.add(n123)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='<b><i>Цветные потолки</i></b>'
                                     '\n\nЯркие цвета способны создать в помещении жизнерадостную '
                                     'атмосферу. \nЦветные натяжные потолки, пользующиеся сегодня '
                                     'большим спросом, неизменно привлекают внимание тех, кто хочет '
                                     'оформить помещение по-настоящему оригинально.'
                                     '\n\n<b>Цена:</b> <u>650 руб/м²</u>'
                                , reply_markup=n2, parse_mode='html')


# single example
@dp.callback_query_handler(lambda c: c.data == 'single_example')
async def usluga(call):
    await types.ChatActions.upload_photo()
    media_multi = types.MediaGroup()
    media_multi.attach_photo('https://i.imgur.com/EK2OZqa.jpg')
    media_multi.attach_photo('https://i.imgur.com/KBuNNyA.jpg')
    media_multi.attach_photo('https://i.imgur.com/g2Ffe2P.jpg', caption='<i>Примеры - Цветные потолки</i>',
                             parse_mode='html')
    await call.message.reply_media_group(media=media_multi)
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    multi_level = types.InlineKeyboardButton('Двухуровневые потолки', callback_data='multi')
    single_level = types.InlineKeyboardButton('Цветные потолки', callback_data='single')
    spaika_poloten = types.InlineKeyboardButton('Матовые потолки', callback_data='spaika')
    apply_level = types.InlineKeyboardButton('Резные потолки Apply', callback_data='apply')
    satinovye = types.InlineKeyboardButton('Сатиновые потолки', callback_data='satinovye')
    picture_on_potolok = types.InlineKeyboardButton('Потолки с фотопечатью',
                                                    callback_data='picture')
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_menu')
    markup2.add(multi_level, single_level, spaika_poloten, picture_on_potolok, apply_level, satinovye)
    markup2.row(n123)
    await call.message.answer(text='У нас есть множество услуг, выберите подходящую вам!',
                              reply_markup=markup2)


# spaika - matovye
@dp.callback_query_handler(lambda c: c.data == 'spaika')
async def usluga123(call):
    n2 = types.InlineKeyboardMarkup(row_width=1)
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_uslugi')
    example = types.InlineKeyboardButton('Посмотреть примеры', callback_data='spaika_example')
    n2.row(example)
    n2.add(n123)
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text='<b><i>Матовые потолки</i></b>'
                                     '\n\nМатовые натяжные потолки идеально имитируют окрашенную или оштукатуренную пов'
                                     'ерхность. Они часто используются в жилых помещениях, позволяют скрыть дефекты '
                                     'основного потолка, сделать комнату более красивой и уютной.'
                                     '\n\n<b>Цена:</b> <u>450 руб/м²</u>'
                                , reply_markup=n2, parse_mode='html')


# spaika-matovye example
@dp.callback_query_handler(lambda c: c.data == 'spaika_example')
async def usluga(call):
    await types.ChatActions.upload_photo()
    media_multi = types.MediaGroup()
    media_multi.attach_photo('https://i.imgur.com/2x8ecrn.jpg')
    media_multi.attach_photo('https://i.imgur.com/plbuy21.jpg')
    media_multi.attach_photo('https://i.imgur.com/SU7Pfhj.jpg', caption='<i>Примеры - Матовые потолки</i>',
                             parse_mode='html')
    await call.message.reply_media_group(media=media_multi)
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    multi_level = types.InlineKeyboardButton('Двухуровневые потолки', callback_data='multi')
    single_level = types.InlineKeyboardButton('Цветные потолки', callback_data='single')
    spaika_poloten = types.InlineKeyboardButton('Матовые потолки', callback_data='spaika')
    apply_level = types.InlineKeyboardButton('Резные потолки Apply', callback_data='apply')
    satinovye = types.InlineKeyboardButton('Сатиновые потолки', callback_data='satinovye')
    picture_on_potolok = types.InlineKeyboardButton('Потолки с фотопечатью',
                                                    callback_data='picture')
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_menu')
    markup2.add(multi_level, single_level, spaika_poloten, picture_on_potolok, apply_level, satinovye)
    markup2.row(n123)
    await call.message.answer(text='У нас есть множество услуг, выберите подходящую вам!',
                              reply_markup=markup2)


# picture
@dp.callback_query_handler(lambda c: c.data == 'picture')
async def usluga(call):
    n2 = types.InlineKeyboardMarkup(row_width=1)
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_uslugi')
    example = types.InlineKeyboardButton('Посмотреть примеры', callback_data='picture_example')
    n2.row(example)
    n2.add(n123)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='<b><i>Потолки с фотопечатью</i></b> '
                                     '\n\nНатяжные потолки с фотопечатью – это технология, при которой на полотно для нат'
                                     'яжного потолка специальными экосольвентными чернилами наносится любое изображение'
                                     '. \nПри этом в качестве основы используют как матовые, так и глянцевые полотна'
                                     '\n\n<b>Цена:</b> <u>1800 руб/м²</u>',
                                reply_markup=n2, parse_mode='html')


# picture example
@dp.callback_query_handler(lambda c: c.data == 'picture_example')
async def usluga(call):
    await types.ChatActions.upload_photo()
    media_multi = types.MediaGroup()
    media_multi.attach_photo('https://i.imgur.com/zUYkgSZ.jpg')
    media_multi.attach_photo('https://i.imgur.com/5E96xub.jpg')
    media_multi.attach_photo('https://i.imgur.com/TbXovxm.jpg', caption='<i>Примеры - Потолки с фотопечатью</i>',
                             parse_mode='html')
    await call.message.reply_media_group(media=media_multi)
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    multi_level = types.InlineKeyboardButton('Двухуровневые потолки', callback_data='multi')
    single_level = types.InlineKeyboardButton('Цветные потолки', callback_data='single')
    spaika_poloten = types.InlineKeyboardButton('Матовые потолки', callback_data='spaika')
    apply_level = types.InlineKeyboardButton('Резные потолки Apply', callback_data='apply')
    satinovye = types.InlineKeyboardButton('Сатиновые потолки', callback_data='satinovye')
    picture_on_potolok = types.InlineKeyboardButton('Потолки с фотопечатью',
                                                    callback_data='picture')
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_menu')
    markup2.add(multi_level, single_level, spaika_poloten, picture_on_potolok, apply_level, satinovye)
    markup2.row(n123)
    await call.message.answer(text='У нас есть множество услуг, выберите подходящую вам!',
                              reply_markup=markup2)


# menu /start
@dp.callback_query_handler(lambda c: c.data == 'nazad_v_menu')
async def usluga(call):
    markup1 = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Услуги", callback_data="usluga")
    button2 = types.InlineKeyboardButton("Связаться с нами", callback_data="feedback")
    button3 = types.InlineKeyboardButton("О нас", callback_data="about_us")
    close = types.InlineKeyboardButton('Закрыть меню', callback_data='close_menu')
    markup1.row(button1)
    markup1.add(button2, button3)
    markup1.row(close)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id
                                , text=f"<i>С возвращением, {call.from_user.first_name}! \nДобро Пожаловать в меню!"
                                       f"\n\nЯ бот помощник компании \"<b>Стройкомплект</b>\""
                                       f"\n\nЧем могу помочь?</i>", parse_mode='html', reply_markup=markup1)


@dp.callback_query_handler(lambda c: c.data == 'close_menu')
async def close_menu(call):
    # await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.delete()
    pass


@dp.callback_query_handler(lambda c: c.data == 'nazad_v_uslugi')
async def usluga(call):
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    multi_level = types.InlineKeyboardButton('Двухуровневые потолки', callback_data='multi')
    single_level = types.InlineKeyboardButton('Цветные потолки', callback_data='single')
    spaika_poloten = types.InlineKeyboardButton('Матовые потолки', callback_data='spaika')
    apply_level = types.InlineKeyboardButton('Резные потолки Apply', callback_data='apply')
    satinovye = types.InlineKeyboardButton('Сатиновые потолки', callback_data='satinovye')
    picture_on_potolok = types.InlineKeyboardButton('Потолки с фотопечатью',
                                                    callback_data='picture')
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_menu')
    markup2.add(multi_level, single_level, spaika_poloten, picture_on_potolok, apply_level, satinovye)
    markup2.row(n123)
    await bot.edit_message_text('У нас есть множество услуг, выберите подходящую вам!', call.message.chat.id,
                                call.message.message_id,
                                reply_markup=markup2)


@dp.callback_query_handler(lambda c: c.data == 'feedback')
async def usluga123(call):
    butts = types.InlineKeyboardMarkup(row_width=2)
    yo1 = types.InlineKeyboardButton('Наш Сайт', url='https://potolki-sk.ru')
    yo2 = types.InlineKeyboardButton('Наша группа Вконтакте', url='https://vk.com/potolki_chita_sk')
    yo3 = types.InlineKeyboardButton('Наш Инстаграм', url='https://www.instagram.com/potolkichita/')
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_menu')
    butts.add(yo1, yo2)
    butts.row(yo3)
    butts.row(n123)
    await bot.edit_message_text(text='Вот наши социальные сети ', chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=butts)


@dp.callback_query_handler(lambda c: c.data == 'about_us')
async def usluga(call):
    markup_us = types.InlineKeyboardMarkup(row_width=1)
    n123 = types.InlineKeyboardButton('Назад', callback_data='nazad_v_menu')
    markup_us.add(n123)
    await bot.edit_message_text(text='<i>Приветствуем вас!</i> \n<i>Мы - компания "<b>Стройкомплект</b>"</i>'
                                     '\n\n<i>В Забайкалье работаем более двенадцати лет и за это время сделали довольными 12400 клиентов.</i> '
                                     '\n\n<i>Благодаря многолетнему опыту работу, выполняем монтаж любой сложности. \n\nИскренне </i>'
                                     '<i>любим своих клиентов и относимся к каждому с заботой и уважением!</i>'
                                     '\n\n<u><i>С уважением, команда "Стройкомплект"</i></u>',
                                chat_id=call.message.chat.id, message_id=call.message.message_id,
                                reply_markup=markup_us, parse_mode='html')


@dp.message_handler(commands=['help'])
async def help(message):
    await message.reply(
        '<i>Вы можете отправить текст:</i> "<code>мой аккаунт</code>", \n<i>чтобы посмотреть данные вашего аккаунта.</i>'
        '\n\n<b>Данные получаются из базы данных, в которую бот сохраняет их при первом взаимодействий с юзером.</b>',
        parse_mode='html')


@dp.message_handler(content_types=['text', 'video', 'audio', 'photo', 'gif', 'sticker', 'voice', 'emoji'])
async def start(message):
    if not message.text.lower() == 'мой аккаунт':
        try:
            conn = sqlite3.connect('potolok_db.db')
            cursor = conn.cursor()
            create_table = cursor.execute('CREATE TABLE IF NOT EXISTS users_of_bot(user_id INTEGER UNIQUE,'
                                          'first_name TEXT,'
                                          'username TEXT'
                                          ');')
            conn.commit()
            add_id = cursor.execute('INSERT INTO users_of_bot VALUES(?,?,?);',
                                    (message.from_user.id, message.from_user.first_name
                                     , message.from_user.username,))
            conn.commit()
            conn.close()
            markup1 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Услуги", callback_data="usluga")
            button2 = types.InlineKeyboardButton("Связаться с нами", callback_data="feedback")
            button3 = types.InlineKeyboardButton("О нас", callback_data="about_us")
            close = types.InlineKeyboardButton('Закрыть меню', callback_data='close_menu')
            markup1.row(button1)
            markup1.add(button2, button3)
            markup1.row(close)
            await message.answer(f"<i>Здравствуйте, {message.from_user.first_name}! \nДобро Пожаловать в меню!"
                                 f"\n\nЯ бот помощник компании \"<b>Стройкомплект</b>\""
                                 f"\n\nЧем могу помочь?</i>", parse_mode='html', reply_markup=markup1)
        except:
            markup1 = types.InlineKeyboardMarkup(row_width=2)
            button1 = types.InlineKeyboardButton("Услуги", callback_data="usluga")
            button2 = types.InlineKeyboardButton("Связаться с нами", callback_data="feedback")
            button3 = types.InlineKeyboardButton("О нас", callback_data="about_us")
            close = types.InlineKeyboardButton('Закрыть меню', callback_data='close_menu')
            markup1.row(button1)
            markup1.add(button2, button3)
            markup1.row(close)
            await message.answer(f"<i>С возвращением, {message.from_user.first_name}! \nДобро Пожаловать в меню!"
                                 f"\n\nЯ бот помощник компании \"<b>Стройкомплект</b>\""
                                 f"\n\nЧем могу помочь?</i>", parse_mode='html', reply_markup=markup1)
    if message.text.lower() == 'мой аккаунт':
        try:
            conn = sqlite3.connect('potolok_db.db')
            cursor = conn.cursor()
            selecting_name = \
            cursor.execute('SELECT first_name FROM users_of_bot WHERE user_id = ?', (message.from_user.id,)).fetchone()[
                0]
            selecting_username = \
            cursor.execute('SELECT username FROM users_of_bot WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            selecting_id = \
            cursor.execute('SELECT user_id FROM users_of_bot WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            await message.answer(f'Ваше Имя  - <a href="http://t.me/{selecting_username}">{selecting_name}</a>'
                                 f'\n\nВаше Имя-пользователя - @{selecting_username}'
                                 f'\n\nВаш id - <code>{selecting_id}</code>', parse_mode='html')
        except Exception as e:
            await message.reply('Произошла ошибка, видимо вас нету в базе данных!')
            print(e)
            pass
    if not message.text:
        await message.reply('К сожалению, я не понимаю ничего кроме текста.'
                            '\n\nМеню бота можно открыть отправив боту любое текстовое сообщение.')
    if message.from_user.id == 421770530:
        if not message.text.lower() == 'мой аккаунт':
            markup_all = types.InlineKeyboardMarkup(row_width=1)
            yes = types.InlineKeyboardButton('Разослать всем', callback_data='yes')
            no = types.InlineKeyboardButton('Отменить рассылку', callback_data='close_menu')
            markup_all.add(yes, no)
            await message.reply(f'{message.text}', reply_markup=markup_all, parse_mode='html')
        if message.text.lower() == 'мой аккаунт':
            try:
                conn = sqlite3.connect('potolok_db.db')
                cursor = conn.cursor()
                selecting_name = \
                    cursor.execute('SELECT first_name FROM users_of_bot WHERE user_id = ?',
                                   (message.from_user.id,)).fetchone()[
                        0]
                selecting_username = \
                    cursor.execute('SELECT username FROM users_of_bot WHERE user_id = ?',
                                   (message.from_user.id,)).fetchone()[0]
                selecting_id = \
                    cursor.execute('SELECT user_id FROM users_of_bot WHERE user_id = ?',
                                   (message.from_user.id,)).fetchone()[0]
                await message.answer(f'Ваше Имя  - <a href="http://t.me/{selecting_username}">{selecting_name}</a>'
                                     f'\n\nВаше Имя-пользователя - @{selecting_username}'
                                     f'\n\nВаш id - <code>{selecting_id}</code>', parse_mode='html')
            except Exception as e:
                await message.reply('Произошла ошибка, видимо вас нету в базе данных!')
                print(e)
                pass


@dp.callback_query_handler(lambda c: c.data == 'yes')
async def yes(call):
    conn = sqlite3.connect('potolok_db.db')
    cursor = conn.cursor()
    users = cursor.execute('''SELECT user_id FROM users_of_bot''').fetchall()
    print(users)
    for i in users:
        try:
            chat_id1 = re.findall(r'\d+', str(i))
            print(chat_id1)
            await bot.copy_message(chat_id=chat_id1[0], message_id=call.message.message_id,
                                   from_chat_id=call.message.chat.id)
        except Exception as e:
            print(e)
            continue
        types.InlineKeyboardButton('', pay=True)
    await call.message.reply(f'Разослано {len(users)} юзерам')
    print(f'Разослано {len(users)} юзерам')
    conn.close()


if __name__ == '__main__':
    executor.start_polling(dp, fast=True, skip_updates=True)
