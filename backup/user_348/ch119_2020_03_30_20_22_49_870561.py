x = 0
n = True
def calcula_euler(x,n):
    x = x + 1
    fat = 1
    while n>1:
        n = n-1
        fat = fat*n
        e = (x**n)/fat
    return e
    

        