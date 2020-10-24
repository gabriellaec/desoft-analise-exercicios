def eh_primo(n):
    primo=True
    i=2
    contador=0
    if n<2:
        primo=False
    else:
        while i<=n:
            if n%i==0:
                contador+=1
            i+=1
        if contador>1:
            primo=False
    return primo

def primos_entre(a,b):
    c=a
    L=[];
    while c<=b:
        if eh_primo(c):
            L.append(c)
        c+=1
    return L