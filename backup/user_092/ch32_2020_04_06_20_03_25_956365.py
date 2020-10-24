def eh_primo(x):
    if x<2:
        return False
    elif x == 2:
        return True
    else:
        t = 2
        while(t<x):
            if (x%t==0):
                return False
            t += 1
        else: 
            return True
def lista_primos(n):
    L = []
    j = n
    e = 2
    while j != len(L):
        if eh_primo(e) == True:
            L.append(e)
        e += 1
    return L
        