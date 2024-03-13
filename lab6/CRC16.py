def crc16(text):
    message = ''
    for symbol in text:
        message += bin(ord(symbol))[2:]
    g = '1000000000000101'
    message = message + '0' * (len(g) - 1)

    word = message[0:len(g)]
    degree = len(g) - 1
    while degree < len(message):
        word = bin(int(word, 2) ^ int(g, 2))[2:]
        while len(word) < len(g):
            degree += 1
            if degree < len(message):
                word += message[degree]
            else:
                return hex(int(word, 2))