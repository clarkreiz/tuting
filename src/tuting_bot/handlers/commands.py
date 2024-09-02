from enum import Enum

from aiogram import types


class Commands(Enum):
    START = ("start", "Главное меню")
    ADD_STUDENT = ("add_student", "Создать нового ученика")
    STUDENT_LIST = ("students_list", "Список учеников")
    CANCEL = ("cancel", "Отменить")

    def __init__(self, code: str, text: str):
        self.code = code
        self.text = text


def make_commands_keyboard() -> types.ReplyKeyboardMarkup:
    row = [types.KeyboardButton(text=command.text) for command in list(Commands)]
    return types.ReplyKeyboardMarkup(keyboard=[row])
