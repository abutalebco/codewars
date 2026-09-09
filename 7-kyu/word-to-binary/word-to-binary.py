def word_to_bin(word):
    # code away!!!
    return [format(ord(char), '08b') for char in word]