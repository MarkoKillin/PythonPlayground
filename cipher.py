class CaesarCipher:

    def __init__(self, shift):
        self.shift = shift

    def cipher(self, input_text):
        output_text = ''
        for letter in input_text:
            c = chr((ord(letter) + self.shift - ord('a')) % 26 + ord('a'))
            output_text += c

        return output_text

    def decipher(self, input_text):
        output_text = ''
        for letter in input_text:
            c = chr((ord(letter) - self.shift - ord('a')) % 26 + ord('a'))
            output_text += c

        return output_text

