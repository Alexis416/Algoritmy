def hash(mini_stroka, bit):
    alphabet = 10
    result = 0
    for i in range(len(mini_stroka)):
        result += int(mini_stroka[i]) * (alphabet ** (bit - i))
    return result


def rabin_karp(stroka, substr):
    substr_len = len(substr)
    stroka_len = len(stroka)
    substr_hash = hash(substr, substr_len - 1)
    count = 0
    for i in range(stroka_len - substr_len + 1):
        stroka_hash = hash(stroka[i: i + substr_len], substr_len - 1)
        if substr_hash == stroka_hash and substr == stroka[i: i + substr_len]:
            count += 1

    return count
