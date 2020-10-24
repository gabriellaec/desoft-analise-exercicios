def eh_primo(x):
    if x==0:
        return False
    elif x==1:
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
    lista=[]
    i=0
    while i>=a and i<=b:
        if eh_primo(i):
            lista.append(i)
            i+=1
        else:
            i+=1
    p=len(lista)
    return p