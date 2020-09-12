def countdown(number):
    if number <= 0:
        return 0

    print(number)
    countdown(number - 1)


countdown(5)
