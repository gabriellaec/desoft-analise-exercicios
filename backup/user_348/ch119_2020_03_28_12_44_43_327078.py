x = 0
n = True
f = 1
def calcula_euler(x,n):
    x = x + 1
    while n>1:
        f *= n
        n = n-1
        e = (x**n)/f
    return e
    

        