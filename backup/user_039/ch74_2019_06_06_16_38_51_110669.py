def conta_bigramas(string):
    dict={}
    b=1
    lista=[]
    for i in string:
        lista.append(string[i]+string[b])
        b+=1
    for x in lista:
        if x not in dict:
            dict[x]=1
        else:
            dict[x]+=1
    return dict
            
        
        
        