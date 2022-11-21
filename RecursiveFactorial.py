def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

y = input("factorial: ")
print(factorial(y))
