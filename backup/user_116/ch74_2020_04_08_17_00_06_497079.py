def conta_bigramas(stri):
    lista=[]
    dici={}
    for n in range(0,len(stri)-1):   
        lista.append(stri[n]+stri[n+1])
    for e in lista:
        dici[e]=lista.count(e) 
    return dici      