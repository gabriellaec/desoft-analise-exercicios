def eh_primo (n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range (3, n, 2):
        if (n%2==0):
            return False 
        elif(n%i == 0):
            return False
    else:
        return True

def primos_entre(a,b):
    lista = []
    p = a
    while p >= a and p <=b:
        if eh_primo(p):
            lista.append(p)
        p = p + 1
    return lista