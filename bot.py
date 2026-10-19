import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⚽ DLS ma'lumotlari", callback_data="info")],
        [InlineKeyboardButton(text="🪙 Coin va Gem do'koni", callback_data="shop")],
        [InlineKeyboardButton(text="📥 Fayllar", callback_data="files")],
        [InlineKeyboardButton(text="👑 Admin panel", callback_data="admin")]
    ])
    await message.answer(
        "⚽ DLS ULTIMATE BOT\n\nKerakli bo'limni tanlang:",
        reply_markup=keyboard
    )

@dp.callback_query()
async def buttons(callback):
    data = callback.data

    if data == "info":
        text = "⚽ DLS bo'yicha maslahatlar va o'yinchilar ma'lumotlari."
    elif data == "shop":
        text = "🪙 Coin va Gem xizmatlari.\nNarxlarni admin belgilaydi."
    elif data == "files":
        text = "📥 DLS uchun ruxsat etilgan fayllar bo'limi."
    elif data == "admin":
        if callback.from_user.id != ADMIN_ID or ADMIN_ID == 0:
            text = "⛔ Bu bo'lim faqat admin uchun."
        else:
            text = "👑 Admin panelga xush kelibsiz."
    else:
        text = "Bo'lim topilmadi."

    await callback.message.answer(text)
    await callback.answer()

async def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN sozlanmagan")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
