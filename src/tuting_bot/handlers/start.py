import aiogram
from aiogram import filters, types

from .commands import make_commands_keyboard

router = aiogram.Router()


@router.message(filters.Command(commands=["start"]))
async def cmd_start(message: types.Message) -> None:
    await message.answer(
        text='Выберите команду для начала. \n\n'
             '/add_student - для добавления нового ученика\n'
             '/student_list - для просмотра всех учеников',
        reply_markup=make_commands_keyboard(),
    )
