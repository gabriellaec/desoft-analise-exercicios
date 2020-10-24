def eh_primo(n):
    primo=True
    i=2
    contador=0
    if n==0 or n==1:
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
    while n<=b:
        if eh primo(c):
            L.append(c)
        n+=1