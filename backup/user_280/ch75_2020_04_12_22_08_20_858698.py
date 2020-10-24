def verifica_primos(lista):
    dicionario = {}
    for x in lista:
        if x==2:
            dicionario[x] = 'True'
        elif x==0 or x==1:
            dicionario[x] = 'False'        
        elif x%2==0:
            dicionario[x] = 'False'
        else:
            n = 3
            while n < x:
                if x%n == 0:
                    dicionario[x] = 'False'
                else:
                    n += 2
        dicionario[x] = 'True'
    return dicionario