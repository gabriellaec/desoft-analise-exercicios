def eh_primo(p):
    if p<2:
        return False 
    elif p==2:
        return True 
    elif p%2==0:
        return False
    else:
        n=3
        while n<p:
            if p%n==0:
                return False
            n+=2
        return True
def verifica_primos(l):
    d = {}
    for i in range(len(l)):
        d[l[i]] = eh_primo(l[i])
    return d