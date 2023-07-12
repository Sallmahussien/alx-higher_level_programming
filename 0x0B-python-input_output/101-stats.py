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
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if count == 10:
                print_info(size, code_dict)
                count = 1
            else:
              count += 1
            line_list = line.split()
            size += int(line_list[-1])
            if line_list[-2] in code_dict:
                code_dict[line_list[-2]] += 1
            else:
                if line_list[-2] in codes:
                  code_dict[line_list[-2]] = 1
    except KeyboardInterrupt:
        print_info(size, code_dict)
        raise
