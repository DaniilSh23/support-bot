from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.emoji import emojize

from keyboards.callback_data import call_base_answer
from keyboards.inline_keyboard import base_questions_inline_formation, head_page_inline_formation
from settings.config import BASE_QUESTIONS_DCT, BOT, ANSWER_FOR_BASE_QUESTIONS_DCT, DP, KEYBOARD


async def base_questions(message: types.Message):
    '''Обработчик для кнопки BASE_QUESTIONS'''

    for i_key, i_value in BASE_QUESTIONS_DCT.items():
        this_message = await BOT.send_message(chat_id=message.chat.id, text='Список вопросов:')
        inline_keyboard = base_questions_inline_formation(i_key, this_message.message_id)
        await this_message.edit_text(text=f'{i_value}', reply_markup=inline_keyboard)


async def answer_the_question(call: CallbackQuery, callback_data: dict):
    '''Ответ на конкретный частозадаваемый вопрос.'''

    await call.answer(text=f'{emojize(":robot:")}Формирую ответ на Ваш вопрос...')
    question_id = callback_data.get('question_id')
    message_id = callback_data.get('message_id')
    question_text = BASE_QUESTIONS_DCT.get(question_id)
    answer_text = ANSWER_FOR_BASE_QUESTIONS_DCT.get(question_id)
    text_for_message = f'<b>Вопрос:</b> {question_text}\n\n' \
                       f'<b>Ответ:</b> {answer_text}'
    inline_keyboard = head_page_inline_formation(message_id)
    await call.message.edit_text(text=text_for_message, reply_markup=inline_keyboard)


def register_base_questions_handlers():
    '''Регистрация обработчиков ответов на стандартные сообщения'''

    DP.register_message_handler(base_questions, Text(equals=KEYBOARD['BASE_QUESTIONS']))
    DP.register_callback_query_handler(answer_the_question, call_base_answer.filter(flag='answer_question'))
