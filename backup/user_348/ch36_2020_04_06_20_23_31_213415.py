#Com for
def fatorial (n):
    fat = 1
    for i in range(n):
        fat=fat*n
        n = n -1
    return fat

#Com while
def fatorial (n):
    fat = 1
    while n > 1:
        fat=fat*n
        n = n -1
    return fat

#Com for.2
def fatorial (n):
    fat = 1
    for i in range(1,n+1):
        fat=fat*i
    return fat