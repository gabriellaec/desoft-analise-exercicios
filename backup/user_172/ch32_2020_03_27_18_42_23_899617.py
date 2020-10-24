n>0
def lista_primos (n):
    if n == 2:
        return True
    elif n == 1 or n == 0:
        return False
    y=3
    while n>2:
        if n%2 == 0:
            return False
        elif n>y and n%y == 0:
            return False
            y=y+2
        else:
            return True
print (lista_primos[2]*n)