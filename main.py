from aiogram import Bot, Dispatcher, types, executor
import random
bot = Bot(token='6393684618:AAEwhh26LagkwVdRxtqtwpiradU-YAL8lpo')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','go'])
async def help(message: types.Message):
    await message.answer(f"Здравстуйте,{message.from_user.full_name} .Меня зовут Tolobrun.\nЕсли хотите узнать обо мне больше нажмите: /help ")
    
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Я могу вам предложить игру << Randomer >>\nПравила игры:\n1) Я угадываю число от 1 до 3 вы должны его отгадать\n2) Писать число только цифрами \n3) Если вы угадываете число вам начисляется по 1 баллу\n4) Не писать текст <<Черный>>\nМои Комманды:\n/start - Запустить бота.\n/help - Помощь.\n/startgame - Начать игру")

@dp.message_handler(text=["1", "2", "3"])
async def hello(message: types.Message):
    try:
        user = int(message.text)
        randomer = random.randint(1, 3)

        await message.answer(f"Удачи вам {message.from_user.full_name}:")

        if user == randomer:
            await bot.send_photo(message.chat.id, photo=open("C:/Users/99677/Desktop/bot/win.jpg", "rb"))
        else:
            await bot.send_photo(message.chat.id, photo=open("C:/Users/99677/Desktop/bot/lose.jpg", "rb"))

    except ValueError:
        await message.answer("Пожалуйста, введите только числа 1, 2 или 3.")

executor.start_polling(dp)
