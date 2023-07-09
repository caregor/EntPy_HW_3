"""
    ---Task 3---
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
"""
from string import punctuation


def count_words(text):
    for char in punctuation:
        text = text.replace(char, "")

    text = text.lower()
    words = text.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    return most_common_words


text = 'Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including ' \
       'structured (particularly procedural), object-oriented and functional programming. It is often described as a ' \
       '"batteries included" language due to its comprehensive standard library.'

most_common_words = count_words(text)
print(most_common_words)
