def calcula_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return calcula_fibonacci(n-1)+calcula_fibonacci(n-2)