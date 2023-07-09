"""
    ---Task 2---
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно
быть дубликатов.
"""


def remove_duplicates(input_list):
    unique_set = set(input_list)
    unique_list = list(unique_set)
    return unique_list


input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9]
result_list = remove_duplicates(input_list)
print(result_list)
