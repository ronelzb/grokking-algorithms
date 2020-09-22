def longest_common_subsequence(s1, s2):
    arr = [[0 for j in range(len(s2))] for i in range(len(s1))]
    longest_subsequence = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                arr[i][j] = 1 + (arr[i - 1][j - 1] if i > 0 and j > 0 else 0)
                longest_subsequence = max(longest_subsequence, arr[i][j])
            else:
                arr[i][j] = max(arr[i - 1][j] if i > 0 else 0, arr[i][j - 1] if j > 0 else 0)

    return longest_subsequence


print(longest_common_subsequence("fish", "fosh"))
