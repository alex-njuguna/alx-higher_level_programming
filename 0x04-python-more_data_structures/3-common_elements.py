#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()

    for item in set_1:
        if item in set_2:
            new_set.add(item)

    return new_set
