n = 1
i = 0
while n < 1001:
    dicionario = {}
    contador = 0
    n = i
    while n > 1:
        if n%2 == 0:
            n = n/2
            contador = contador + 1
        else:
            n = 3*n + 1
            contador = contador + 1
    dicionario[i] = contador 
    n = n + 1

print (max(dicionario, key = dicionario.get))
    
        