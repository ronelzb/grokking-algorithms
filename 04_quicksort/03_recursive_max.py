import sys


def recursive_max(input_list):
    if not input_list:
        return -sys.maxsize

    return max(input_list[0], recursive_max(input_list[1:]))


print(recursive_max([2, 4, 5, 6, 7, 8, 10]))
