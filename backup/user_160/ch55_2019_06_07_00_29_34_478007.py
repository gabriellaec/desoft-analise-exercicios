def eh_primo(x):
    if x < 2:
        return False
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    elif x % 2 !=0:
        i = 3
        while i < x:
            if x % i != 0:
                i = i + 2
            elif x % i == 0: 
                return False
        return True

def primos_entre(a, b):
    contador = 0
    p = a
    lista = []
    while p >= a and p <= b:
        if eh_primo(p) == True:
            lista.append(p)
            p += 1
    
        else:
            p += 1
    return lista