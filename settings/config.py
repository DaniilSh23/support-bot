import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from emoji import emojize

# токен выдается при регистрации приложения
TOKEN = os.environ.get('TOKEN', '5265303938:AAE1daGp-VJR0R15J9tHksR38hQlbCXMYdU')

# Телеграм ID админов
ADMINS_ID_LST = [1978587604]
STAFF_ID = 1978587604

# абсолютный путь до текущей директории этого файла
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# кнопки управления
KEYBOARD = {
    'BASE_QUESTIONS': emojize(':red_question_mark: Частозадаваемые вопросы'),
    'MY_PROBLEM': emojize(':safety_vest: Решить мою проблему'),
    'HEAD_PAGE': emojize(":house_with_garden: Главная"),
    'ANSWER': emojize('✅ ОТВЕТ'),

    'X_ORDER': emojize('❌ ОТМЕНИТЬ ЗАКАЗ'),
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}

# объекты: бот, диспатчер, сторэдж для машины состояний
BOT = Bot(token=TOKEN, parse_mode='HTML')
STORAGE = MemoryStorage()
DP = Dispatcher(BOT, storage=STORAGE)

# частозадаваемые вопросы
BASE_QUESTIONS_DCT = {
    '1': f'{emojize(":red_question_mark:")}Первый частозадаваемый вопрос',
    '2': f'{emojize(":red_question_mark:")}Второй частозадаваемый вопрос',
    '3': f'{emojize(":red_question_mark:")}Третий частозадаваемый вопрос',
    '4': f'{emojize(":red_question_mark:")}Четвертый частозадаваемый вопрос',
}
ANSWER_FOR_BASE_QUESTIONS_DCT = {
    '1': f'{emojize(":information:")}Ответ на первый частозадаваемый вопрос',
    '2': f'{emojize(":information:")}Ответ на второй частозадаваемый вопрос',
    '3': f'{emojize(":information:")}Ответ на третий частозадаваемый вопрос',
    '4': f'{emojize(":information:")}Ответ на четвёртый частозадаваемый вопрос',
}

