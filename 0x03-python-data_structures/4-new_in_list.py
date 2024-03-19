#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''replaces an element in a list at a specific position

    without modifying the original list'''
    if idx < 0 or idx > (len(my_list) - 1):
        return my_listi.copy()
    else:
        list = []
        for number in my_list:
            list.append(number)
        list[idx] = element
        return list
