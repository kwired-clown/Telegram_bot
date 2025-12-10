import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    logger.error("Токен не найден! Установи TELEGRAM_BOT_TOKEN в Railway")
    raise ValueError("Токен не найден")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я бот-учитель Python!\n\n"
        "📚 Команды:\n"
        "/start - приветствие\n"
        "/help - помощь\n"
        "/python - основы Python\n"
        "/code - примеры кода\n"
        "/author - автор бота\n\n"
        "Создатель: @Sense_livee"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Помощь:\n\n"
        "Этот бот учит Python с нуля!\n\n"
        "💡 Команды:\n"
        "/python - уроки по основам\n"
        "/code - рабочие примеры\n"
        "/author - контакты автора\n\n"
        "❓ Вопросы: @Sense_livee\n"
        "🐍 Удачи в изучении Python!"
    )

async def python_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐍 ОСНОВЫ PYTHON:\n\n"
        "1. Вывод на экран:\n"
        "   print('Привет, мир!')\n\n"
        "2. Переменные:\n"
        "   name = 'Иван'\n"
        "   age = 15\n\n"
        "3. Условия:\n"
        "   if age >= 18:\n"
        "       print('Взрослый')\n"
        "   else:\n"
        "       print('Подросток')\n\n"
        "💡 Практикуйся на replit.com"
    )

async def code_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💻 ПРИМЕР КОДА - КАЛЬКУЛЯТОР:\n\n"
        "def calculator():\n"
        "    a = float(input('Первое число: '))\n"
        "    b = float(input('Второе число: '))\n"
        "    op = input('Операция (+, -, *, /): ')\n"
        "    \n"
        "    if op == '+':\n"
        "        return a + b\n"
        "    elif op == '-':\n"
        "        return a - b\n"
        "    elif op == '*':\n"
        "        return a * b\n"
        "    elif op == '/':\n"
        "        if b != 0:\n"
        "            return a / b\n"
        "        else:\n"
        "            return 'Ошибка: деление на ноль'\n"
        "    else:\n"
        "        return 'Неизвестная операция'\n\n"
        "Попробуй запустить этот код!"
    )

async def author_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👨‍💻 АВТОР БОТА:\n\n"
        "• Создатель: @Sense_livee\n"
        "• Бот создан для обучения Python\n"
        "• Полный код на GitHub\n\n"
        "💌 По вопросам пиши: @Sense_livee"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if 'привет' in text:
        await update.message.reply_text("И тебе привет! 👋")
    elif 'python' in text:
        await update.message.reply_text("Python — лучший язык! 🐍\nНапиши /python для уроков")
    elif 'спасибо' in text:
        await update.message.reply_text("Всегда рад помочь! 😊")
    else:
        await update.message.reply_text(
            "Я лучше объясню Python! 🤖\n\n"
            "Напиши:\n"
            "/python - уроки\n"
            "/code - примеры кода\n"
            "/help - помощь"
        )

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("python", python_cmd))
    app.add_handler(CommandHandler("code", code_cmd))
    app.add_handler(CommandHandler("author", author_cmd))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    logger.info("🚀 Бот запускается на Railway...")
    print("🤖 PYTHON TEACHER BOT")
    print("👨‍💻 Автор: @Sense_livee")
    
    app.run_polling()

if __name__ == "__main__":
    main()
