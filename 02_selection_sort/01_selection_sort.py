def find_smallest(unsorted_list):
    smallest = unsorted_list[0]
    smallest_index = 0

    for i in range(1, len(unsorted_list)):
        if unsorted_list[i] < smallest:
            smallest = unsorted_list[i]
            smallest_index = i

    return smallest_index


def selection_sort(unsorted_list):
    new_list = []

    for i in range(len(unsorted_list)):
        smallest_index = find_smallest(unsorted_list)
        new_list.append(unsorted_list.pop(smallest_index))

    return new_list


print(selection_sort([5, 3, 6, 2, 10]))
