#!/usr/bin/python3
def roman_to_int(roman_string):
    '''Converts a Roman numeral to an integer'''
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    previous_value = 0

    for char in roman_string:
        if char in roman:
            current_value = roman[char]
            total += current_value
            if current_value > previous_value:
                total -= 2 * previous_value
            previous_value = current_value

    return total
