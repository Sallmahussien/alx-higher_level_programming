#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    num, idx, length = 0, 0, len(roman_string)

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    while idx < length:
        current_value = roman_dict[roman_string[idx]]

        if roman_string[idx] not in roman_dict:
            return 0

        if idx != length-1 and current_value < roman_dict[roman_string[idx+1]]:
            num += current_value * -1
        else:
            num += current_value
        idx += 1
    return num
