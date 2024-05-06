from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def main_menu_keyboard():
    main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='My To Do List', callback_data="ToDoList")],
        [InlineKeyboardButton(text='Додати', callback_data="Add")],
        [InlineKeyboardButton(text='Вилучити', callback_data="Delete")]])
    return main_keyboard


def button_back():
    button = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="back", callback_data="BACK")]
    ])
    return button
