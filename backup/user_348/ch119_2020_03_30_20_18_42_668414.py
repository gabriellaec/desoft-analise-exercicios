x = 0
n = True
def calcula_euler(x,n):
    x = x + 1
    f = 1
    while n>1:
        n = n-1
        f = f*n
        e = (x**n)/f
    return e
    

        