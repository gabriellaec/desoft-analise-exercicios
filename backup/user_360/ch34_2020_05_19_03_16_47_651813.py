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
def maior_primo_menor_que(n):
    i = n
    nenhum = -1
    while i>0:
        w = eh_primo(i)
        if w == True:
            return i
        i = i-1
    return nenhum
