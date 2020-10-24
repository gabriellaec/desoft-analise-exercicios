def fatorial(n):
    if n < 0:
        return 0
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total
        
        