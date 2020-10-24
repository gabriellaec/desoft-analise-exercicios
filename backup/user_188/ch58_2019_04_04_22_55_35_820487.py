def calcula_fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = calcula_fibonacci(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst