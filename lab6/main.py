from CRC16 import crc16
from multiplication import hash_multiplication

text = input("Введите текст: ")
print("Выберете метод хэширования: \n"
      "1. Умножение \n"
      "2. CRC-16 ")
choice = input("Введите номер: ")

if choice == "1":
    text_hash = hash_multiplication(text)
    print(text_hash)
    print(f"Количество слов: {len(text_hash)}")
elif choice == "2":
    text_hash = crc16(text)
    print(text_hash)
