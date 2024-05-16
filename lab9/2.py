def counting_sort(arr, reverse=False):
    # Определение размера алфавита
    alphabet_size = 1500

    # Создание массива для подсчета частоты символов
    count = [0] * alphabet_size

    # Подсчет частоты символов в массиве
    for char in arr:
        for i in range(len(char)):
            count[ord(char[i])] += 1

    # Создание отсортированного массива
    sorted_arr = []
    for i in range(alphabet_size):
        sorted_arr.extend([chr(i)] * count[i])

    # Возвращение отсортированного массива в зависимости от направления сортировки
    if reverse:
        return sorted_arr[::-1]
    else:
        return sorted_arr


# Примеры тестовых случаев
arr1 = ["apple", "banana", "cherry"]
arr2 = ["Привет", "World", "Python"]
arr3 = []
arr4 = ["a", "b", "c", "A", "B", "C"]

# Сортировка массива по возрастанию
sorted_arr1 = counting_sort(arr1)
print(sorted_arr1)

# Сортировка массива по убыванию
sorted_arr2 = counting_sort(arr2, reverse=True)
print(sorted_arr2)

# Сортировка пустого массива
sorted_arr3 = counting_sort(arr3)
print(sorted_arr3)

# Сортировка массива с учетом регистра символов
sorted_arr4 = counting_sort(arr4)
print(sorted_arr4)
