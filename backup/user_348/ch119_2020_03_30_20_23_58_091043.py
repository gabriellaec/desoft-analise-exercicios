x = 0
n = True
def fatorial (n):
    fat = 1
    while n > 1:
        fat=fat*n
        n = n -1
    return fat

def calcula_euler(x,n):
    x = x + 1
    fat = 1
    while n>1:
        n = n-1
        e = (x**n)/fat
    return e
    

        