def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    loe = [elem for elem in arr[1:] if elem <= pivot]
    gt = [elem for elem in arr[1:] if elem > pivot]
    return quicksort(loe) + [pivot] + quicksort(gt)


print(quicksort([6, 4, 3, 2, 1]))
