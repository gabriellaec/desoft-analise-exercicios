def verifica_primos(lista):
    i=2
    primos={}
    while i<len(lista):
        n=1
        while n < i:
            if i % n == 0 and n != 1:
                primos[i]='0'
                n=i
            else:
                n+=1
            if n==(i-1) and i % n != 0:
                primos[i]='1'
                n=i
        i+=1
    return primos 