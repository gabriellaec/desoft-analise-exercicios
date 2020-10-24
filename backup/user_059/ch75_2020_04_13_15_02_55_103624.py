def eh_primo(x):
    if x<2:
        return False
    elif x==2:
        return True
    else:
        if x%2==0: 
            return False
        else:
            i = 3
            while i<x:
                if x%i == 0:
                    break
                i+=1
            if i==x:
                return True
            else:
                return False 

def verifica_primos(l):
    d = {}
    for i in range(len(l)):
        d[l[i]] = eh_primo(l[i])
    return d