def binary_search(sorted_list, item):
    # mid = len(sorted_list) / 2
    left_pointer = 0
    right_pointer = len(sorted_list) - 1
    steps = 0

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2
        mid_num = sorted_list[mid]

        if mid_num == item:
            return mid
        elif mid_num < item:
            left_pointer = mid + 1
        else:  # mid_num < item
            right_pointer = mid - 1

        steps += 1

    return None


test_list = [2, 3, 5, 6, 8, 10, 12, 15, 18, 24, 27, 29]
print(binary_search(test_list, 19))
