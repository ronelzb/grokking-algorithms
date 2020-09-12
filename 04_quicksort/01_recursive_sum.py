def loop_sum(input_list):
    if len(input_list) == 0:
        return 0
    elif len(input_list) == 1:
        return input_list[0]

    return input_list[-1] + input_list.pop(-1)


print(loop_sum([2, 4, 6]))
