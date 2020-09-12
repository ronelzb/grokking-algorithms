def recursive_count(input_list):
    if not input_list:
        return 0

    return 1 + recursive_count(input_list[1:])


print(recursive_count([2, 4, 5, 6, 7, 8, 10]))
