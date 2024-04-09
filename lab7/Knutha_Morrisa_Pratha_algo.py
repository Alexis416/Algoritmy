def fun_pref(substr):
    result = [0] * len(substr)
    j = 0
    i = 1
    while i < len(substr):
        if substr[j] == substr[i]:
            result[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                result[i] = 0
                i += 1
            else:
                j = result[j - 1]
    return result


def knuth_morris_prath(stroka, substr):
    substr_len = len(substr)
    stroka_len = len(stroka)
    fun_prefix = fun_pref(substr)
    count = 0
    i = 0
    j = 0
    while i < stroka_len:
        if stroka[i] == substr[j]:
            if j == substr_len - 1:
                count += 1
                j = fun_prefix[j]
            else:
                j += 1
            i += 1
        elif j > 0:
            j = fun_prefix[j-1]
        else:
            i += 1
    return count
