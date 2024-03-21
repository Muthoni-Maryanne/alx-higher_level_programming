#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''deletes keys with a specific value in a dictionary'''
    new_dict = {}
    new_list = []

    if value not in a_dictionary.values():
        return a_dictionary

    for k, v in a_dictionary.items():
        if v is value:
            new_list.append(k)
            for key in new_list:
                del a_dictionary[key]
            new_dict[k] = v
        return new_dict
