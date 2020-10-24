def conta_bigramas(string):
    dict={}
    a=0
    b=1
    lista=[]
    for i in string:
        lista.apend(lista[a]+lista[b])
        a+=1
        b+=1
    for x in lista:
        if x not in dict:
            dict[x]=1
        else:
            dict[x]+=1
    return dict
            
        
        
        