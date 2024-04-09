from timeit import default_timer
from Naivniy_algo import naive
from Rabina_Karpa_algo import rabin_karp
from Boyera_Moora_algo import boyer_moore
from Knutha_Morrisa_Pratha_algo import knuth_morris_prath


def search_substring(algorithm_of_search):
    fibo = [0, 1]
    for i in range(2, 500):
        fibo.append(fibo[i - 1] + fibo[i - 2])

    fibo = [str(i) for i in fibo]
    fib_str = ''.join(fibo)

    max_num = '00'
    max_count = 0
    time = default_timer()
    for i in range(10):
        for j in range(10):
            curr_substr = str(i) + str(j)
            curr_count = algorithm_of_search(fib_str, curr_substr)
            if curr_count > max_count:
                max_count = curr_count
                max_num = curr_substr

    time_search = default_timer() - time
    print(f"Самая часто встречающаяся комбинация 2 цифр: {max_num}")
    print(f"Количество раз, которое она встретилась: {max_count}")
    print("Время поиска:", time_search)


while True:
    algorithm = input("Выбери8те алгоритм поиска:\n"
                      "1. Наивный алгоритм\n"
                      "2. Алгоритм Рабина-Карпа\n"
                      "3. Алгоритм Бойера-Мура\n"
                      "4. Алгоритм Кнута-Морриса-Пратта\n")

    if algorithm == "1":
        search_algorithm = naive
    elif algorithm == "2":
        search_algorithm = rabin_karp
    elif algorithm == "3":
        search_algorithm = boyer_moore
    elif algorithm == "4":
        search_algorithm = knuth_morris_prath
    elif algorithm == "exit":
        break
    else:
        print("Неправильный ввод")
        continue

    search_substring(search_algorithm)
