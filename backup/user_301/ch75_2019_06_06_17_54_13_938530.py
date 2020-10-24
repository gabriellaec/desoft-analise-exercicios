def verifica_primos(lista):
    dc=dict()
    i=0
    n=1
    while i<=len(lista):
        if lista[i]%(lista[i]-n)==0:
            
       