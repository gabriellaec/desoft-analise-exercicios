def primos_entre(a, b):
    lista=[]
    for n in range(a, b+1):
        div=3
        if n%2==0 and n!=2 or n==1 or n==0:
            n+=1
        while n > div:
            if n%div==0:
                n+=1
            div +=2
        lista.append(n)
    lista.sort()
    return lista
        
        