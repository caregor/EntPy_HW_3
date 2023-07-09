"""
    ---Task 4---
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.

    *Верните все возможные варианты комплектации рюкзака.
"""
BACKPACK_CAPACITY = 10


def choose_all_items(backpack_capacity, items):
    all_variants = []

    def find_variants(current_variant, remaining_capacity, remaining_items):
        if remaining_capacity < 0:
            return

        if remaining_capacity == 0:
            all_variants.append(current_variant)
            return

        if not remaining_items:
            return

        item = remaining_items[0]
        item_name, item_weight = item

        if item_weight <= remaining_capacity:
            find_variants(current_variant + [item_name], remaining_capacity - item_weight, remaining_items[1:])

        find_variants(current_variant, remaining_capacity, remaining_items[1:])

    find_variants([], backpack_capacity, list(items.items()))

    return all_variants


def choose_items(backpack_capacity, items):
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    chosen_items = []
    total_weight = 0

    for item in sorted_items:
        if total_weight + item[1] <= backpack_capacity:
            chosen_items.append(item[0])
            total_weight += item[1]

    return chosen_items


items = {
    'Тент': 3,
    'Спальник': 2,
    'Котелок': 1,
    'Фонарик': 2,
    'Палатка': 4,
    'Еда': 5
}

chosen_items = choose_items(BACKPACK_CAPACITY, items.items())
print("Выбранные вещи для рюкзака:", chosen_items)
print()

all_variants = choose_all_items(BACKPACK_CAPACITY, items)
print("Все варианты выбранных вещей:")
for variant in all_variants:
    print(variant)
