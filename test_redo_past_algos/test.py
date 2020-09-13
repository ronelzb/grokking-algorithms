def binary_search(arr, elem):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value == elem:
            return mid
        elif mid_value < elem:
            left = mid + 1
        else:  # mid_value > elem
            right = mid - 1

    return None


print(binary_search([2, 3, 5, 6, 8, 9, 10, 12, 13, 15, 18], 3))
