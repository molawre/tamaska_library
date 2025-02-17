import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Твой токен
TOKEN = "7614471703:AAGkQNzzzgk_ALeTt0vTS2tWEu8YN-EaUz8"

# Список вариантов и ссылок
options = {
    "🔹 Olimpbet (КЗ)": "https://www.dropbox.com/scl/fo/cfihid5fyrve6bxn873mf/AJ6cstN_zNRAp_ZguqSURcI?rlkey=9o0nj0w04bn4rsujl82itqrkf&dl=0",
    "🔸 Olimpbet (РФ)": "https://www.dropbox.com/scl/fo/3zsz5r8fopd5wqg0wr9tl/AFkpDgYVdBn1up28axSGZQc?rlkey=qjt0apfoxdvgaoc2k4y12x4pq&dl=0",
    "🔹 OLYMP Casino": "https://www.dropbox.com/scl/fo/7z4iapkz8xha6y9hjbc73/AMF1x8bYwbuWaibYNCEx_Oc?rlkey=oxnamdjc9vwe7wdcodih152wi&dl=0",
    "🔸 Batery": "https://www.dropbox.com/scl/fo/83o9cp3tejg06ig75zc8o/AND8bUwBMoByk-CXUsG_z_I?rlkey=oipfctpzt34skzerjsj23vh1g&dl=0",
    "🔹 Batery AI": "https://www.dropbox.com/scl/fo/2pi1aokvv2ruy2lkblwqf/ALN1r_6xy3Q9rSSlHz79Dpc?rlkey=joebtxkk0mvljc9y9b3xu1usu&dl=0",
    "🔸 Onion (казино РФ)": "https://www.dropbox.com/scl/fo/xncnec9jwi5vas1e4ska9/AOyC9J1lJQ6DdCNQlsreV94?rlkey=ui5wz7npwi8gr3qbrzkdw87fg&dl=0",
    "🔹 PinUP Casino": "https://www.dropbox.com/scl/fo/rtjw31tt9sfbi58y42m1o/AAD-6gfA-icROYNOzEh2FqY?rlkey=pzfnau0q9y39dm3h2dcduv125&dl=0",
    "🔸 1XBET": "https://www.dropbox.com/scl/fo/gz3ugt07ech1pfna97aec/AJsQIxiF-z1I9kHUufRZrtg?rlkey=g8u7p5lf4yuomahl7k98j4g2r&dl=0",
    "🔹 1XBAT": "https://www.dropbox.com/scl/fo/rk1pqb1gdss95uf043lxd/ANV57uuN8IKZiXyxOdO0mAU?rlkey=zb74qivpzh4az3kta1sjuh6kq&dl=0",
    "🔸 1XSLOTS": "https://www.dropbox.com/scl/fo/7xyrquvhcve01miwfzs0f/AMkwUcJGSAVNqaTe_B9kpZA?rlkey=iqsp6hosq3n8c5ic1u23ej8zg&dl=0",
    "🔸 22Bet": "https://www.dropbox.com/scl/fo/7qg3jl7x20o51pbzx5o36/ABeNouHBkVaPAClr77pIj0k?rlkey=4tzxhbhe8t8avqipsqpd33v81&dl=0",
    "🔹 22Bat": "https://www.dropbox.com/scl/fo/c9s3icduiy2ckk27ttbpi/AMDlfhKplfnGZ-a2e0eM50Q?rlkey=qlmmqg8ngby50k8oxjtjz78vh&dl=0",
    "🔸 Betwinner": "https://www.dropbox.com/scl/fo/cljk5taweswiblt1fe93v/AHr6zb1OmLPxSDLduXplZFY?rlkey=xfzxtsodcaz4zz2rztmsbrqe7&dl=0"





    
}

# Логирование
logging.basicConfig(level=logging.INFO)

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создаем клавиатуру с вариантами (внизу экрана)
reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=name)] for name in options.keys()],
    resize_keyboard=True
)

# Хэндлер для /start
@dp.message(lambda message: message.text == "/start")
async def send_welcome(message: types.Message):
    await message.answer("Выберите вариант:", reply_markup=reply_keyboard)

# Обработчик выбора варианта
@dp.message(lambda message: message.text in options)
async def send_link(message: types.Message):
    link = options[message.text]
    await message.answer(f"🔗 {message.text}: {link}")

# Запуск бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Убираем Webhook
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
