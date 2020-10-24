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
P = []
for e in range(400):
    if eh_primo(e) == True:
            P.append(e)
def lista_primos(n):
    L = []
    for e in range(n):
        L.append(P[e])
    return L
        