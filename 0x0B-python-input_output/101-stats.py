#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys


def process_line(line, occurrences_obj, itr_num, file_size):
    """Process a line and update occurrences_obj."""
    line = line.split(' ')

    if len(line) != 9:
        return 0, 0

    if line[7] in occurrences_obj:
        occurrences_obj[line[7]] += 1

    itr_num += 1
    file_size += int(line[8])

    return itr_num, file_size


def print_statistics(file_size, occurrences_obj):
    """Print file size and non-zero occurrences_obj statistics."""
    print(f"File size: {file_size}")

    non_zero_items = {key: value for key, value
                      in occurrences_obj.items() if value != 0}

    sorted_items = sorted(non_zero_items.items(), key=lambda x: x[0])

    for key, value in sorted_items:
        print(f'{key}: {value}')


def main():
    """Starting point for the log parser"""
    itr_num = 0
    occurrences_obj = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    file_size = 0

    try:
        for line in sys.stdin:
            itr_num, file_size = process_line(line,
                                              occurrences_obj,
                                              itr_num,
                                              file_size)

            if itr_num % 10 == 0:
                print_statistics(file_size, occurrences_obj)

        print_statistics(file_size, occurrences_obj)

    except KeyboardInterrupt:
        print_statistics(file_size, occurrences_obj)
        raise


if __name__ == '__main__':
    main()
