def fatorial(n):

    if n == 1 or n == 0:
        return 1

    else:
        total = n*(n-1)
        n -= 2

        while n != 0:
            total = total * n
            n -= 1
        return total