def factorial(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1

    return x * factorial(x - 1)


print(factorial(4))