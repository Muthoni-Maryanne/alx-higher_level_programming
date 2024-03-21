#!/usr/bin/python3
def best_score(a_dictionary):
    '''returns a key with the biggest integer value'''
    if a_dictionary is None or not a_dictionary:
        return None

    max_key = ''
    max_value = 0

    for k, v in a_dictionary.items():
        if v > max_value:
            max_value = v
            max_key = k

    return max_key
