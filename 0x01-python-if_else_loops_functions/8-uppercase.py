#!/usr/bin/python3
def uppercase(str):

    for char in str:
        if 97 <= ord(char) <= 122:
            new_char = chr(ord(char) - 32)
        else:
            new_char = char
        print(new_char, end='')

