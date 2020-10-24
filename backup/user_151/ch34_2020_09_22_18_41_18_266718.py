def eh_primo(x):
    if x == 0 or x == 1:
        return False
    elif x % 2 == 0 and x != 2:
        return False
    elif x == 2 or x == 3:
        return True
    else:
        z = 1
        y = 2*z + 1
        while y < x:
            if x % y == 0:
                return False
                break
            else:
                z = z + 1
                y = 2*z + 1
        if x == y:
            return True

def lista_primos(n):
    lista = [0]*n
    i = 0
    j = 0
    while j<n :
        if eh_primo(i):
            lista[j]=i
            j = j + 1
        i = i + 1
    print(j)
    return lista
    

def primos_entre(a, b):
    i = a
    j = 0
    while i<=b :
        if eh_primo(i):
            j = j + 1
        i = i + 1
    return j

def maior_primo_menor_que(n):
    lista = [0]*primos_entre(0, n)
    i = 0
    j = 0
    if n < 2:
        return -1
    while i<=n :
        if eh_primo(i):
            lista[j]=i
            j = j + 1
        i = i + 1
    return lista[j-1]