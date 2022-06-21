from aiogram.utils.callback_data import CallbackData


call_head_page = CallbackData('@', 'message_id', 'flag')
call_base_answer = CallbackData('@', 'question_id', 'flag', 'message_id')
