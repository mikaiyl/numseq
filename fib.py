def fib(n):
    if n is 0:
        return 0
    elif n is 1:
        return 1
    index = 0
    result = [0]
    a, b = 0, 1
    while index < n:
        result.append(b)
        a, b = b, a+b
        index += 1
    return result[-1]
