def factorial(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))
