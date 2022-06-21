from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data import call_head_page, call_base_answer
from settings.config import KEYBOARD


def head_page_inline_formation(message_id):
    '''Формирователь клавиатуры(кнопки) для перехода на главную.'''

    inline_keyboard = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=KEYBOARD['HEAD_PAGE'],
                        callback_data=call_head_page.new(
                            flag='head_page',
                            message_id=message_id,
                        )
                    )
                ],
            ]
            )
    return inline_keyboard


def base_questions_inline_formation(question_id, message_id):
    '''Формирователь клавиатуры для менеджера.'''

    inline_keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=KEYBOARD['ANSWER'],
                        callback_data=call_base_answer.new(
                            flag='answer_question',
                            question_id=question_id,
                            message_id=message_id
                        )
                    )
                ],
            ]
            )
    return inline_keyboard
