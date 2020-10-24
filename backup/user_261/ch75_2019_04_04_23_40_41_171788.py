def verifica_primos(lista):
    d={}
    primo=True
    i=0
    e=2
    while i<len(lista):
        if lista[i]%e==0:
            primo=False
        d[lista[i]]=primo
        i+=1
        e+=1
    return d
   
            
