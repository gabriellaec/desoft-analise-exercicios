def acha_bigramas(string):
    i=1
    lista=[]
    while i < len(string):
        
       	lista.append(string[i-1:i])
        i+=1
    return lista