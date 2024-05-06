from aiogram.fsm.state import State, StatesGroup

class AddTask(StatesGroup):
    taskAdd = State()

class DelTask(StatesGroup):
    taskDelete = State()
