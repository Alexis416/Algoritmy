def get_key(word):
    result = 0
    for i in word:
        result += ord(i)
    return result


def hash_multiplication(text):
    text_list = text.split()
    len_mas = len(text_list)
    text_keys = []
    C = 0.4
    for word in text_list:
        text_keys.append(len_mas * ((get_key(word) * C) % 1))
    return text_keys
