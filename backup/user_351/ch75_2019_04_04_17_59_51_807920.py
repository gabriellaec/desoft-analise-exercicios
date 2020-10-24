def verifica_primos(lista):
    dicionario={}
    i = 0
    lista[i]=int(lista[i])
    while i <len(lista):
        divisor = 2
    	primo = True
        if lista[i]<2:
            dicionario[lista[i]] = False
        elif lista[i]==2:
            dicionario[lista[i]] = True
        else:
            while divisor <lista[i]:
                if lista[i]%divisor == 0:
                    primo = False
                divisor+=1
            dicionario [lista[i]] = primo
        i+=1
    return dicionario