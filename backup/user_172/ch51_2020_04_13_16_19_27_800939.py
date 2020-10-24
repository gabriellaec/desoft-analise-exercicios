def eh_primo(x):
    if x == 2:
        return True
    elif x == 1 or x == 0:
        return False
    y=3
    while x>2:
        if x%2 == 0:
            return False
        elif x == y:
            return True
        elif x>y and x%y == 0:           
            return False            
        else:
            y+=2
    return True

def primos_entre (a,b):
    lista = []
    p = 0
    while b-a>=0:
        if eh_primo(a) == True:
            p == eh_primo(a)
            lista.append(p)
            a += 1
        else:
            a += 1
        print(lista)
    return lista