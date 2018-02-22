def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(1, n):
        result *= k
    return result

f5 = factorial(10)  # f5 = 120