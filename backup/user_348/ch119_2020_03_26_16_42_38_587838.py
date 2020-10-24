x = 0
n = True
def calcula_euler(x,n):
    x = x + 1
    while n:
        e = (x**n)/n!
        return e
        