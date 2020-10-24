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

def primos_entre(a,b):
    t=0
    i=a
    while i<=b:
        if eh_primo(i):
            t+=1
        i+=1
    return t