import asyncio
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton

API_TOKEN = 'YOUR_API_TOKEN'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    kb = [
        [types.KeyboardButton(text="Узнать цену криптовалюты💰")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer(f"{message.from_user.full_name}, Добро пожаловать в криптобота!", reply_markup=keyboard)
    await message.answer('Воспользуйтесь кнопкой для того, чтобы узнать цену')


@dp.message(F.text == 'Узнать цену криптовалюты💰')
async def cmd_random(message: types.Message):
    # Add buttons for popular cryptocurrencies
    ikb = [
        [InlineKeyboardButton(text="Bitcoin", callback_data="BTC"),
         InlineKeyboardButton(text="Ethereum", callback_data="ETH")],
        [InlineKeyboardButton(text="Binance Coin", callback_data="BNB"),
         InlineKeyboardButton(text="Ripple", callback_data="XRP")],
        [InlineKeyboardButton(text="Cardano", callback_data="ADA"),
         InlineKeyboardButton(text="Solana", callback_data="SOL")],
        [InlineKeyboardButton(text="Dogecoin", callback_data="DOGE"),
         InlineKeyboardButton(text="Polygon", callback_data="MATIC")],
        [InlineKeyboardButton(text="Litecoin", callback_data="LTC")]
    ]
    # **Corrected line:** Ensure "inline_keyboard" is included with the correct value
    ikeyboard = types.InlineKeyboardMarkup(inline_keyboard=ikb, resize_keyboard=True)

    await message.answer(
        "Выберите криптовалюту:",
        reply_markup=ikeyboard
    )


@dp.callback_query(lambda c: c.data in ["BTC", "ETH", "LTC", "BNB", "XRP", "ADA", "SOL", "DOGE", "MATIC"])
async def callback_handler(call: types.CallbackQuery):
    crypto_name_map = {
        "BTC": "Bitcoin",
        "ETH": "Ethereum",
        "LTC": "Litecoin",
        "BNB": "Binance Coin",
        "XRP": "Ripple",
        "ADA": "Cardano",
        "SOL": "Solana",
        "DOGE": "Dogecoin",
        "MATIC": "Polygon",
    }
    default_name = crypto_name_map[call.data]
    crypto_name = call.data
    price = await get_price(default_name, crypto_name)
    await call.message.answer(f"{price}", parse_mode="HTML")


async def get_price(default_name, crypto_name):
    url_usdt = f"https://api.binance.com/api/v3/avgPrice?symbol={crypto_name}USDT"
    url_rub = f"https://api.binance.com/api/v3/avgPrice?symbol={crypto_name}RUB"

    response_usdt = requests.get(url_usdt)
    response_rub = requests.get(url_rub)

    if response_usdt.status_code == 200 and response_rub.status_code == 200:

        if crypto_name in ["BTC", "LTC", "ETH", "BNB"]:
            price_usdt = round(float(response_usdt.json()['price']), 2)
        else:
            price_usdt = round(float(response_usdt.json()['price']), 4)
        price_rub = round(float(response_rub.json()['price']), 2)
        message = f"<b>Цена {default_name}✅</b>\n<code>{price_usdt} $ 🇱🇷</code>\n<code>{price_rub} ₽ 🇷🇺</code>"
        return message
    else:
        return "Ошибка при получении цены."


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
