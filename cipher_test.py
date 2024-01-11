import cipher


def ciphering():
    input_text = input('Input text you want to cipher: ')
    shift = 0
    try:
        shift = int(input('Input shift: '))
    except ValueError:
        shift = 0
    print('Your text: ' + input_text)
    cph = cipher.CaesarCipher(shift)
    ciphered_text = cph.cipher(input_text)
    print('Ciphered text: ' + ciphered_text)
    deciphered_text = cph.decipher(ciphered_text)
    print('Deciphered text: ' + deciphered_text)


if __name__ == '__main__':
    ciphering()
