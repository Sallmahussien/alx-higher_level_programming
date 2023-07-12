#!/usr/bin/python3
'''Reads stdin line by line and computes metrics'''
import sys


def print_info(size, code_dict):
    '''Prints some info'''
    print('File size: {:d}'.format(size))

    for key in sorted(code_dict):
        print('{}: {:d}'.format(key, code_dict[key]))


if __name__ == "__main__":
    count = 0
    size = 0
    code_dict = {}

    for line in sys.stdin:
        if count == 10:
            print_info(size, code_dict)
            count = 0
            size = 0
            code_dict = {}
        count += 1
        line_list = line.split()
        size += int(line_list[-1])
        if line_list[-2] in code_dict:
            code_dict[line_list[-2]] += 1
        else:
            code_dict[line_list[-2]] = 1
