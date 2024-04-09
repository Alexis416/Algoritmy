def boyer_moore(stroka, substr):
    len_substr = start_str = substr_pointer = stroka_pointer = len(substr)
    count = 0
    while start_str <= len(stroka):
        while substr_pointer > 0:
            if stroka[stroka_pointer - 1] == substr[substr_pointer - 1]:
                stroka_pointer -= 1
                substr_pointer -= 1
            elif start_str == len(stroka):
                return count
            else:
                start_str += 1
                substr_pointer = len_substr
                stroka_pointer = start_str
        if substr_pointer <= 0:
            count += 1
            start_str += 1
            substr_pointer = len_substr
            stroka_pointer = start_str
    return count
