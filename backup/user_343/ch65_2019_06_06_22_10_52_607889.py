def acha_bigramas(string):
    i=0
    lista=[]
    while i < len(string):
        
       	lista.append(string[i:len(string):2])
        i+=1
    return lista

