#!/usr/bin/python3
def remove_char_at(str, n):

    mystr = ''
    i = 0
    for char in str:
        if i != n:
            mystr += char
        i += 1
    return mystr
