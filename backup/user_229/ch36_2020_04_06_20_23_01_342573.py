total = 0
def fatorial(n):
    for i in range(n):
        total = total*i
        i += 1
    return total
print(fatorial)