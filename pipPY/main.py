# py -m pip install isodd # ввод клманды в терминале для загрузки библиотек, 
# где последнее слово(isodd) это название ,загружаемой библиотеки
# pip freeze
# pip freeze >requirements.txt / комманды для сохранения библиотек подгруженных
# pip  install -r  requirements.txt / комманда для загрузки сохраненных библиотек(чаще необходимо другому программисту который будет работать с кодом )
# pip  install python-telegram-bot --upgrade
# botfather. найти в телеграмме
# выбрать комманду newbot.
# Написать название бота чтобы в конце было 'bot'
# скопировать токен (HTTP API)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello{update.effective_user.first_name}')


app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()