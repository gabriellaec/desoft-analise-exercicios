def eh_primo(x):
    if x==0 or x==1:
        return False
    elif x==2:
        return True
    elif x%2==0:
        return False
    else:
        i=3
        while i<x:
            if x%i==0:
                return False
            i+=2
        return True

def maior_primo_menor_que(n):
    t=n
    while t<=n:
        if eh_primo(t):
            break
        t-=1
    if n<2:
        t=-1
    return t