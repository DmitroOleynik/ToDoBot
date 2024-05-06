from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app.keyboards import main_menu_keyboard, button_back
from app.data import *
from app.fsm import AddTask, DelTask
from aiogram.fsm.context import FSMContext


user_router = Router()


@user_router.message(CommandStart())
async def commandStarts(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        f"Вітаю {message.from_user.full_name}\nкоманда для виклику головного меню - /main"
        )
            
@user_router.callback_query(F.data == "ToDoList")
async def myList(callback: CallbackQuery):
    await callback.message.answer(
        read_json(callback.from_user.id), reply_markup=button_back()
        )

@user_router.message(Command("main"))
async def mainMenu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "ГОЛОВНЕ МЕНЮ", reply_markup=main_menu_keyboard()
    )

@user_router.callback_query(F.data == "Add")
async def addTask(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(AddTask.taskAdd)
    await callback.message.answer(
        "Введіть завдання для додавання", reply_markup=button_back()
        )

@user_router.message(AddTask.taskAdd)
async def add(message: Message, state: FSMContext):
    data = await state.update_data(taskAdd=message.text)
    await message.answer(
        save_task_json(message.from_user.id, data["taskAdd"])
    )
    return await mainMenu(message, state)
    
@user_router.callback_query(F.data == "Delete")
async def deleteTask(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(DelTask.taskDelete)
    await callback.message.answer(
        f"Введіть завдання для видалення\n{read_json(callback.from_user.id)}", reply_markup=button_back()
    )

@user_router.message(DelTask.taskDelete)
async def delete(message: Message, state: FSMContext):
    data = await state.update_data(taskDelete=message.text)
    await message.answer(
        delete_task_json(message.from_user.id, data["taskDelete"])
    )
    return await mainMenu(message, state)

@user_router.callback_query(F.data == "BACK")
async def commandBack(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete()
    return await mainMenu(callback, state)
    
@user_router.message()
async def notUnderstand(message: Message):
    await message.answer(
        "Я цей... як його...\nне андерстенд вас"
        )     
