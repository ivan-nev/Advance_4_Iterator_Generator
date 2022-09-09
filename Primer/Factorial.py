def factorial_2(x):
    if x == 1:
        return 1
    else:
        return x * factorial_2(x - 1)

print(factorial_2(5))  # 120