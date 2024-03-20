#!/usr/bin/python3
def best_score(a_dictionary):
    '''returns a key with the biggest integer value'''
    if a_dictionary is None or not a_dictionary:
        return None
    else:
        return max(a_dictionary)
