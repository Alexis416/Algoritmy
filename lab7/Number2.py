import re

import docx
import wikipedia


def normal_stroka(string):
    stroka_without_spec = re.sub('[^А-ЯЁа-яёA-Za-z\s]+', '', string).lower()
    stroka_with_normal_space = re.sub('[\s]+', ' ', stroka_without_spec)
    normalize_stroka = stroka_with_normal_space.replace('ё', 'е')
    return normalize_stroka


def get_ord(symbol):
    if symbol != " ":
        return ord(symbol) - 1072
    return 33


def hash_fun(word):
    hash = 0
    for s in word:
        hash += hash * 42 + get_ord(s)
    return hash


document = docx.Document("Астероид.docx")
par_in_text = []
for paragraph in document.paragraphs:
    par_in_text.append(paragraph.text)

text = normal_stroka(' '.join(par_in_text))

wikipedia.set_lang("ru")
wiki_page = normal_stroka(wikipedia.page("Астероид").content)

text = text.split(" ")
wiki_page = wiki_page.split(" ")

text_three = [" ".join(text[i: i + 3]) for i in range(len(text) - 2)]
hash_text_three = []
for three in text_three:
    hash_text_three.append(hash_fun(three))

wiki_page_three = [" ".join(wiki_page[i: i + 3]) for i in range(len(wiki_page) - 2)]
hash_wiki_page_three = []
for three in wiki_page_three:
    hash_wiki_page_three.append(hash_fun(three))
hash_wiki_page_three = set(hash_wiki_page_three)

count_of_words = 0
last_three_plagiat = False
for three in hash_text_three:
    if three in hash_wiki_page_three:
        if last_three_plagiat:
            count_of_words += 1
        else: count_of_words += 3
        last_three_plagiat = True
    else:
        last_three_plagiat = False

print(f"Количество слов в реферате: {len(text)}")
print(f"Количество одинаковых с Википедией слов: {count_of_words}")
print(f"Плагиат: {round(100 * count_of_words / len(text), 2)}%")
