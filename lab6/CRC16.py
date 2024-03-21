def crc16(text):
    message = ''
    for symbol in text:
        message += bin(ord(symbol))[2:]
    g = '1000000000000101'
    message = message + '0' * (len(g) - 1)

    word = message[0:len(g)]
    index = len(g) - 1
    while index < len(message):
        word = bin(int(word, 2) ^ int(g, 2))[2:]
        while len(word) < len(g):
            index += 1
            if index < len(message):
                word += message[index]
            else:
                return hex(int(word, 2))
