def primos_entre(a, b):
    i=2
    intervalo=[]
    primos=[]
    c=a
    while c<=b:
        intervalo.append(b-c)
        c+=1
    
    contador=0
    n=intervalo[contador]
    
    while i<n:
        if n==0 or n==1:
            n+=1
        if n%i==0:
            primos.append(n)
        i+=1
        n+=1
    return True