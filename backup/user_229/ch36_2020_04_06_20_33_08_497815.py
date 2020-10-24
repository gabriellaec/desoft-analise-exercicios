def fatorial(n):
    total = 0
    for i in range(1,n+1):
        total = total*i
        i += 1
    print(total)
    return total
