def verifica_primos(x):
    numero=[1,2,3,4,5,6,7,8,9,13,995]
    dicionario={}
    for i in range(len(numero)):
        if numero[i]==1:
            dicionario[numero[i]] = False
        elif numero[i]==2:
            dicionario[numero[i]] = False
        elif numero[i]==3:
            dicionario[numero[i]] = False
        
        if numero[i]%2 !=0 and numero[i]%3 !=0 and numero[i]%5 !=0:
            dicionario[numero[i]] = False
            
        else:
            dicionario[numero[i]] = True
    return dicionario