#!/usr/bin/python3
def no_c(my_string):

    letters = []
    for character in my_string:
        letters.append(character)

    for i in range(len(letters) - 1, -1, -1):
        if letters[i] == 'c' or letters[i] == 'C':
            letters.pop(i)

    return ''.join(letters)
