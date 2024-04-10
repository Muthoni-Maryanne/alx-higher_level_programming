#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''function that prints x elements of a list'''
    try:
        i = 0
        j = 0

        '''get len of list'''
        for element in my_list:
            j += 1

        '''print elements specified'''
        while i < x:
            print(my_list[i], end='')
            i += 1
        print()

        '''raise IndexError if out of range'''
        if x > j:
            raise IndexError

        return x

    except IndexError:
        return j
    except Exception as e:
        return 0
