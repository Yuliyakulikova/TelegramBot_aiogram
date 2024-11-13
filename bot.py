import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F


# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Замените YOUR_TOKEN_HERE на ваш токен
API_TOKEN = '7893696227:AAEzbpd7CmwW-td_jWkgMRgQwURXWf6pyyw'

# Создаем объекты бота и диспетчера с хранилищем состояний
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Используем хранилище в памяти
dp = Dispatcher(storage=storage)

# Обработчик команды /start
@dp.message(F.command("start"))
async def command_start(message: types.Message):
    await message.reply("Привет! Я ваш бот. Чем могу помочь?")

# Обработчик текстовых сообщений
@dp.message()
async def echo(message: types.Message):
    await message.reply(message.text)

# Функция для запуска бота
async def main():
    await dp.start_polling(bot)

# Запуск бота
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())