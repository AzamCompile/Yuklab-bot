import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import yt_dlp

# Bot tokenini o'zingizniki bilan almashtiring
TOKEN = "8418649553:AAG8X6ualdBWlf40LcesVqFolwzTEV4HFVw"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Start komandasi
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Salom 👋 Menga YouTube yoki Instagram link yuboring, men sizga yuklab beraman!")

# Link yuborilganda ishlaydi
@dp.message()
async def download_handler(message: types.Message):
    url = message.text.strip()

    # faqat link bo'lsa
    if not url.startswith("http"):
        await message.answer("❌ Bu linkga o‘xshamaydi.")
        return

    await message.answer("⏳ Yuklab olinmoqda, biroz kuting...")

    try:
        ydl_opts = {
        "outtmpl": "D:\Новая папка (3)\Новая папка%(title)s.%(ext)s",
        "format": "mp4/bestaudio/best",
}


        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info)

        # Foydalanuvchiga faylni yuboramiz
        await message.answer_document(types.FSInputFile(file_name))

    except Exception as e:
        await message.answer(f"⚠️ Xato: {e}")

# Asosiy funksiya
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
