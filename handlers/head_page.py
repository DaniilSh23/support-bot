import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.emoji import emojize

from keyboards.callback_data import call_head_page, call_base_answer
from keyboards.inline_keyboard import head_page_inline_formation
from keyboards.reply_keyboard import MAIN_MENU
from settings.config import DP, KEYBOARD, ADMINS_ID_LST, BOT
from states.base_states import SupportMessageState


async def start_command_handler(message: types.Message):
    '''Реакция бота на команду /start'''

    text_for_message = f'{emojize(":robot:")} <b>Здравствуйте</b>, Вас приветствует бот техподдержки.\n\n' \
                       f'{emojize(":service_dog:")}<b>Я Ваш верный друг</b> в решения самых разных проблем.\n' \
                       f'{emojize(":rescue_worker’s_helmet:")}С удовольствием помогу, если у Вас возникли стандартные трудности и в любых необычных ситуациях.'
    await message.answer(text=text_for_message, reply_markup=MAIN_MENU)


async def head_page(call: CallbackQuery, callback_data: dict, state: FSMContext):
    '''Реакция бота на инлайн кнопку ГЛАВНАЯ.'''

    await state.reset_state()
    await call.answer(text=f'{emojize(":robot:")}Вы перешли на главную')
    text_for_message = f'{emojize(":robot:")}<b>Вы находитесь на главной</b>\n\n'\
                       f'{emojize(":service_dog:")}<b>Всегда готов</b> оказать помощь в любой ситуации.\n'
    await call.message.answer(text=text_for_message, reply_markup=MAIN_MENU)


async def my_problem(message: types.Message):
    '''Реакция на нажатие кнопки MY_PROBLEM'''

    await message.answer(text=f'{emojize(":robot:")}Слушаю Ваш вопрос...', reply_markup=ReplyKeyboardRemove())
    text_for_message = f'{emojize(":robot:")}Отправте следующим сообщением описание Вашей ситуации.\n\n' \
                       f'{emojize(":man_technologist:")}Наш менеджер <b>займётся поиском решения</b> и свяжется с Вами.\n\n'
    inline_keyboard = head_page_inline_formation(message.message_id)
    await message.answer(text=text_for_message, reply_markup=inline_keyboard)
    # задаю пользователю состояние
    await SupportMessageState.users_message.set()


async def send_users_message(message: types.Message, state: FSMContext):
    '''Обработчик при получении обращения пользователя.'''

    user_appeal = message.text
    # сохраняем в машину состояния обращение пользователя (здесь это не обязательно, для демонстрации)
    # также не обязательно передавать словарь, но явное лучше, чем неявное
    await state.update_data(
        {
            'user_appeal': user_appeal,
        }
    )
    # ответ пользователю и кнопка ГЛАВНАЯ
    inline_keyboard = head_page_inline_formation(message.message_id)
    await message.answer(text=f'{emojize(":robot:")}Принял Ваше обращение, адресую менеджеру для обработки...', reply_markup=inline_keyboard)

    # пересылка рандомному менеджеру обращения пользователя
    manager = random.choice(ADMINS_ID_LST)
    # inline_manager_keyboard = user_appeal_inline_formation()
    await BOT.send_message(chat_id=manager,
                           text=f'{emojize(":robot:")}<b>ПОЛУЧЕНО НОВОЕ ОБРАЩЕНИЕ</b>{emojize(":bellhop_bell:")}\nПересылаю...')
    await message.forward(chat_id=manager)

    # для ДЕМОНСТРАЦИИ БОТА отправка всем, кто написал их же сообщений
    await BOT.send_message(chat_id=manager,
                           text=f'{emojize(":robot:")}<b>ПОЛУЧЕНО НОВОЕ ОБРАЩЕНИЕ</b>{emojize(":bellhop_bell:")}\nПересылаю...')
    await message.forward(chat_id=message.chat.id)

    # сбросить состояние пользователя
    await state.finish()


def register_head_page_handlers():
    DP.register_message_handler(start_command_handler, Command(['start', 'help']))
    DP.register_message_handler(my_problem, Text(equals=KEYBOARD['MY_PROBLEM']))
    DP.register_callback_query_handler(head_page, call_head_page.filter(flag='head_page'), state=SupportMessageState.users_message)
    DP.register_callback_query_handler(head_page, call_head_page.filter(flag='head_page'))
    DP.register_message_handler(send_users_message, state=SupportMessageState.users_message)
