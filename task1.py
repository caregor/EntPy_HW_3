"""
    ---Task 1---
    Задача №8
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""


def find_common_items(friends):
    common_items = set.intersection(set(friends['Друг 1']),set(friends['Друг 2']),set(friends['Друг 3']))
    return common_items


def find_unique_items(friends):
    all_items = set.union(*(set(items) for items in friends.values()))
    common_items = find_common_items(friends)
    unique_items = all_items - common_items
    return unique_items


def find_missing_items(friends):
    missing_items = {}
    for friend, items in friends.items():
        other_friends = set()
        for name in friends:
            if name != friend:
                other_friends.update(friends[name])
        missing = other_friends - items
        if missing:
            missing_items[friend] = missing
    return missing_items


friends = {
    'Друг 1': {'рюкзак', 'палатка', 'спальник'},
    'Друг 2': {'рюкзак', 'палатка', 'фонарик', 'еда'},
    'Друг 3': {'рюкзак', 'палатка', 'карта', 'компас'}
}

common_items = find_common_items(friends)
print("Вещи, которые взяли все три друга:", common_items)

unique_items = find_unique_items(friends)
print("Уникальные вещи, есть только у одного друга:", unique_items)

missing_items = find_missing_items(friends)
for friend, items in missing_items.items():
    print("У друга", friend, "отсутствуют вещи:", items)
