from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from config import Token
from aiogram.types import ContentTypes, Message


TOKEN = "5702488906:AAHhvnPWucJ9feswh64pTyhmuVLuNBi8FX8"

HELP_COMMAND = '''
<b>/start</b>-<em>старт бота</em>
<b>/description</b>-<em>+мораль</em
'''

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/description'))
kb.add(KeyboardButton('1.v при равноуск.движ.'))
kb.add(KeyboardButton('2.v при равномерн.движ.'))
kb.add(KeyboardButton('3.S при равномерн.движ.'))
kb.add(KeyboardButton('4.S при равноуск.движ.'))
kb.add(KeyboardButton('5. ускорение'))
kb.add(KeyboardButton('6. второй з-н Ньютона'))
kb.add(KeyboardButton('7. третий з-н Ньютона'))
kb.add(KeyboardButton('8. силы в механике'))
kb.add(KeyboardButton('9. з-н сохранения импульса'))
kb.add(KeyboardButton('10. з-н сохранения энергии'))
kb.add(KeyboardButton('11. мощность и мех.работа'))
kb.add(KeyboardButton('12. момент силы'))
kb.add(KeyboardButton('13. сила Архимеда'))
kb.add(KeyboardButton('14. основное уравнение МКТ'))
kb.add(KeyboardButton('15. кол-во вещ-ва'))
kb.add(KeyboardButton('16. число молекул'))
kb.add(KeyboardButton('17. концентрации молекул'))
kb.add(KeyboardButton('18. средняя кинетическая энергия'))
kb.add(KeyboardButton('19. уравнение Менделеева-Клапейрона'))
kb.add(KeyboardButton('20. уравнение Клапейрона'))
kb.add(KeyboardButton('21. изопроцессы'))
kb.add(KeyboardButton('22. внутренняя энергия газа'))
kb.add(KeyboardButton('23. работа газа'))
kb.add(KeyboardButton('24. первое начало термодинамики'))
#kb.add(KeyboardButton('25. формулы кпд'))
kb.add(KeyboardButton('26. законы Кулона'))
kb.add(KeyboardButton('27. напряженность электрического поля'))
kb.add(KeyboardButton('28. работа электростатичского поля'))
kb.add(KeyboardButton('29. потенциал электрического поля'))
kb.add(KeyboardButton('30. электроемкость заряженного проводника, конденстаторов различной формы'))
kb.add(KeyboardButton('31. энергия электрического поля'))
kb.add(KeyboardButton('32. з-ны Ома для участка и полной цепи'))
kb.add(KeyboardButton('33. формулы силы тока'))
kb.add(KeyboardButton('34. параллельное и последовательное соед. проводников'))
kb.add(KeyboardButton('35. мощность электрического тока'))
kb.add(KeyboardButton('36. з-н Джоуля-Ленца'))
kb.add(KeyboardButton('37. работа тока'))

bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Я запустился!')

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать!',
                           reply_markup=kb)

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode='HTML')


@dp.message_handler(commands=['description'])
async def command_desc(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Ты справишься с зачетом =)',)


@dp.message_handler(text='1.v при равноуск.движ.')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://shareslide.ru/img/thumbs/b2097407be4df43b0a8569d151757194-800x.jpg')

@dp.message_handler(text='2.v при равномерн.движ.')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://ondoclub.ru/800/600/https/ds04.infourok.ru/uploads/ex/027a/001090c1-21c9a109/img4.jpg')

@dp.message_handler(text='3.S при равномерн.движ.')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://mypresentation.ru/documents_6/f540cd163944fb280933ee553969181b/img5.jpg')

@dp.message_handler(text='4.S при равноуск.движ.')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://istinaved.ru/uploads/attach/12031/717df9949857e85b545d.jpg')
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://studfile.net/html/2706/1128/html_0_bIOP1Unp.QvUr/htmlconvd-HnxMSh_html_52d11abab298eddd.gif')

@dp.message_handler(text='5. ускорение')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://aybaz.ru/wp-content/uploads/3/7/7/377839239daf96489fa7476f0e17e744.webp')


@dp.message_handler(text='6. второй з-н Ньютона')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://cf3.ppt-online.org/files3/slide/v/VrMf8Dl6BFH7XvCw5u1NKxkAI03LRUqYg2tPTZ/slide-8.jpg')


@dp.message_handler(text='7. третий з-н Ньютона')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://cf2.ppt-online.org/files2/slide/o/OBqzJHyWIS0K9Z8nhTdt625QDsL4EFVi1GMwCbNfY/slide-17.jpg')

@dp.message_handler(text='8. силы в механике')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://s0.slide-share.ru/s_slide/6322fbbebc4c2e8dbd4591b4fa4ceef2/3d9a1564-2acd-433c-ae64-a52743cd7078.jpeg')

@dp.message_handler(text='9. з-н сохранения импульса')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://skazka-arkhyz.ru/wp-content/uploads/6/4/c/64cbe160b492aaf11d69f38b846e6b5c.jpeg')

@dp.message_handler(text='10. з-н сохранения энергии')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='http://images.myshared.ru/116/1437379/slide_12.jpg')

@dp.message_handler(text='11. мощность и мех.работа')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://profgbo.ru/wp-content/uploads/5/4/8/548d5e6ab6a466da81e6520d93042549.jpeg')
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='http://www.school.nd.ru/articles/mon/iumk/files/COR_Physics_7/4_energy/4_01/images/05.JPG')

@dp.message_handler(text='12. момент силы')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='http://images.myshared.ru/17/1140949/slide_8.jpg')

@dp.message_handler(text='13. сила Архимеда')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://csri.ru/800/600/https/ru-static.z-dn.net/files/d91/28d9ab8cffe1a182a82587a6f131e9a5.jpg')

@dp.message_handler(text='14. основное уравнение МКТ')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://prezentacii.org/upload/cloud/19/01/119568/images/screen5.jpg')

@dp.message_handler(text='15. кол-во вещ-ва')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://cdn-user84060.skyeng.ru/uploads/61caaf177cc2e067545237.png')

@dp.message_handler(text='16. число молекул')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://myslide.ru/documents_3/e30cd78b73a2668cbb61d94bf928a67b/img33.jpg')

@dp.message_handler(text='17. концентрации молекул')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://studfile.net/html/2706/1078/html_79utqDhGd0.ZNJE/img-GQqtL9.png')

@dp.message_handler(text='18. средняя кинетическая энергия')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://student-madi.ru/wp-content/uploads/2020/04/f49070763bca4cd7198f55ac7c3fac16.jpg')

@dp.message_handler(text='19. уравнение Менделеева-Клапейрона')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://prezentacii.org/upload/cloud/18/05/50285/images/screen2.jpg')

@dp.message_handler(text='20. уравнение Клапейрона')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://studfile.net/html/2706/975/html_Sw4ZeLHzE2.3CaC/htmlconvd-84XooW_html_2d882abe3fa3e077.gif')

@dp.message_handler(text='21. изопроцессы')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://cf3.ppt-online.org/files3/slide/u/Ux68hZzqL74BECbJmnRcANpydTGvDow5VaWPKl/slide-5.jpg')

@dp.message_handler(text='22. внутренняя энергия газа')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://fs.znanio.ru/d5af0e/61/6d/c281bf9a1a584adfe875b71dc7d965595e.jpg')
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://cf.ppt-online.org/files1/slide/e/ENlfZxz6cvTYDyRoenkAbpQUmMPaSIJWsHjXg2rCGF/slide-13.jpg')

@dp.message_handler(text='23. работа газа')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://fs.znanio.ru/d5af0e/5f/01/dedd75c6ac5dfac0bd01217f722b8b62a4.jpg')

@dp.message_handler(text='24. первое начало термодинамики')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://cf2.ppt-online.org/files2/slide/q/q6ey0YDbcuKgRNUjfzmVoH7XdFLn5BWxCAMwl4/slide-9.jpg')

#@dp.message_handler(text='25. формулы кпд')
#async def send_photo(message: Message):
 #   chat_id = message.from_user.id
  #  await dp.bot.send_photo(chat_id=message.from_user.id,
   #                         photo='https://ondoclub.ru/800/600/https/ds04.infourok.ru/uploads/ex/0492/00124089-6b902213/img14.jpgg')

@dp.message_handler(text='26. законы Кулона')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://ledsshop.ru/wp-content/uploads/9/2/0/9209dd5a5aa34dfb31b5a021cc3beee4.jpeg')

@dp.message_handler(text='27. напряженность электрического поля')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://profgbo.ru/wp-content/uploads/e/8/1/e8109785e237e43ab1a131915461b1fa.jpeg')

@dp.message_handler(text='28. работа электростатичского поля')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://present5.com/presentation/30863916_437429168/image-14.jpg')

@dp.message_handler(text='29. потенциал электрического поля')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://physik.ucoz.ru/_ph/15/712699818.gif')

@dp.message_handler(text='30. электроемкость заряженного проводника, конденстаторов различной формы')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://uk-parkovaya.ru/wp-content/uploads/0/8/6/086ef710d8a76a073acaa3dfaab94bd6.jpg')

@dp.message_handler(text='31. энергия электрического поля')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://uk-parkovaya.ru/wp-content/uploads/1/3/f/13f637f8154b8aeea7e6ad45bbf0e8c0.jpg')

@dp.message_handler(text='32. з-ны Ома для участка и полной цепи')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://yarllo.ru/wp-content/uploads/4/2/8/4286b2480faa3bf00e7631f5f2ec9abe.jpeg')

@dp.message_handler(text='33. формулы силы тока')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://electro-scooterz.ru/wp-content/uploads/d/1/2/d12ff3cbf3289752066350d9d23fefd9.jpeg')

@dp.message_handler(text='34. параллельное и последовательное соед. проводников')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://kelmochka.ru/wp-content/uploads/2021/12/parallelnoe-soedinenie-rezistorov-36.jpg')

@dp.message_handler(text='35. мощность электрического тока')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='http://uznaikak.ru/wp-content/uploads/2018/10/2_formula-moshhnost-jelektricheskogo-toka.jpg')

@dp.message_handler(text='36. з-н Джоуля-Ленца')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://yarllo.ru/wp-content/uploads/a/8/1/a814c181f438397537d5bf1d874d6c6d.jpeg')

@dp.message_handler(text='37. работа тока')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='https://ledsshop.ru/wp-content/uploads/d/4/1/d4134ea78865c7e44beda076d5175ce2.jpeg')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)










#@dp.message_handler(commands=['help'])
#async def help_command(message: types.Message):
 #   await bot.send_message(chat_id=message.from_user.id, text='HELP_COMMAND', parse_mode='HTML')
  #  await message.delete()


#@dp.message_handler(commands=['формула'])
#async def send_image(message: types.Message):
 #   await bot.send_photo(chat_id=message.chat.id,
  #                       photo='https://ondoclub.ru/800/600/https/ds04.infourok.ru/uploads/ex/027a/001090c1-21c9a109/img4.jpg')
