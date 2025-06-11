import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from dotenv import load_dotenv

from handlers import register_handlers
from dialogs import name_dialog

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Получаем токен из .env файла
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    """Основная функция для запуска бота"""
    if not BOT_TOKEN:
        logging.error("BOT_TOKEN не найден в .env файле!")
        return
    
    # Создаем бота и диспетчер
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Регистрируем диалог
    dp.include_router(name_dialog)
    
    # Настраиваем диалоги
    setup_dialogs(dp)
    
    # Регистрируем обработчики
    register_handlers(dp)
    
    logging.info("Бот запущен!")
    
    # Запускаем бота
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logging.info("Бот остановлен пользователем")
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())