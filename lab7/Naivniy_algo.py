def naive(stroka, substr):
    count = 0
    for i in range(len(stroka) - 1):
        if stroka[i] == substr[0] and stroka[i + 1] == substr[1]:
            count += 1
    return count