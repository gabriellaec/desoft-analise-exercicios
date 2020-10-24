def conta_bigramas(string):
    dict={}
    b=0
    i=1
    lista=[]
    while i<len(string):
        lista.append(string[b]+string[i])
        b+=1
        i+=1
    for x in lista:
        if x not in dict:
            dict[x]=1
        else:
            dict[x]+=1
    return dict
            
        
        
        