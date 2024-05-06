import json
import datetime


def notification(user_id):
    if read_json_dict(str(user_id)) != {}:
        now = datetime.datetime.now()
        if now.hour == 14 and now.minute == 0:
            return "Там же завдання не виконані є..."


def read_json_dict(user_id):
    with open("app/data/users.json", encoding="utf-8") as fileJson:
        data = json.load(fileJson)
        if str(user_id) not in data["users"]:
            return {}
        else:
            return data["users"][str(user_id)]
    

def read_json(user_id):
    with open("app/data/users.json", encoding="utf-8") as fileJson:
        data = json.load(fileJson)
        stringiterator = "Ваш список завдань:\n"
    if str(user_id) not in data["users"]:
        return "Вас ще немає в базі користувачів(напишіть перше завдання)"
    else:
        if data['users'][str(user_id)] != {}:
            for item in data["users"][str(user_id)].values():
                stringiterator += item + "\n"
            return stringiterator
        else:
            return "У вас немає завдань(напишіть завдання)"


def save_task_json(user_id, task):
    if task[0] == "/":
        return "ймовірно це команда, команда не може бути завданням"
    else:
        with open("app/data/users.json", encoding="utf-8") as filejson:
            dict_data = json.load(filejson)
        if str(user_id) not in dict_data["users"]:
            dict_data["users"][str(user_id)] = {}
        with open("app/data/users.json", "w", encoding="utf-8") as filejson:
            dict_data['users'][str(user_id)][str(datetime.datetime.now())] = task
            json.dump(dict_data, filejson, ensure_ascii=False, indent=4)
        return f"Завдання {task} успішно додано"


def delete_task_json(user_id, value_task):
    if value_task[0] == "/":
        return f"Завдання {value_task} немає у списку"
    else:
        with open("app/data/users.json", encoding='utf-8') as filejson:
            dict_data = json.load(filejson)
            if value_task not in dict_data['users'][str(user_id)].values():
                return "Нажаль, такого завдання немає "
            else:
                for key, value in list(dict_data["users"][str(user_id)].items()):
                    if value == value_task:
                        del dict_data["users"][str(user_id)][key]
        with open("app/data/users.json", "w", encoding='utf-8') as filejson:
            json.dump(dict_data, filejson, ensure_ascii=False, indent=4)
            return f"Завдання '{value_task}' успішно видаленно"
