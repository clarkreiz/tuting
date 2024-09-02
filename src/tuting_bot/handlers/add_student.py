import logging

import aiogram
from aiogram import filters, types
from aiogram.fsm import context, state

from .commands import Commands as cmds

router = aiogram.Router()


class StudentRegistration(state.StatesGroup):
    waiting_for_name = state.State()
    waiting_for_age = state.State()


@router.message(filters.Command(commands=[cmds.ADD_STUDENT.code]))
@router.message(aiogram.F.text.in_(cmds.ADD_STUDENT.text))
async def cmd_add_student(message: types.Message, state: context.FSMContext) -> None:
    await state.set_state(StudentRegistration.waiting_for_name)

    await message.answer(text='Введите имя студента')

    logging.info(f"User {message.from_user.id} started adding student: {message.text}")

@router.message(StudentRegistration.waiting_for_name)
async def process_name(message: types.Message, state: context.FSMContext) -> None:
    user_name = message.text

    if len(user_name) < 2:
        await message.answer(text='Имя не должно быть короче 2 символов, попробуйте снова.')
        return

    await state.update_data(name=user_name)

    await state.set_state(StudentRegistration.waiting_for_age)

    logging.info(f"User {message.from_user.id} entered student name: {user_name}")

    await message.answer(text='Введите возраст студента')

@router.message(StudentRegistration.waiting_for_age)
async def process_age(message: types.Message, state: context.FSMContext) -> None:
    try:
        user_age = int(message.text)
        if user_age <= 0 or user_age >= 100:
            raise ValueError("Age must be between 1 and 99.")
    except ValueError:

        await message.answer('Введите корректный возраст (от 1 до 99).')

        return

    await state.update_data(age=user_age)

    user_data = await state.get_data()

    await state.clear()

    await message.answer(
        text=f"Студент {user_data['name']} с возрастом {user_data['age']} добавлен."
    )

    logging.info(f"User {message.from_user.id} entered student age: {user_data['age']}")
