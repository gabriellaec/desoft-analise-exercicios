def fatorial(n):
    total = 1
    for i in range(1,n):
        total = total*i
        i += 1
    print(total)
    return total
