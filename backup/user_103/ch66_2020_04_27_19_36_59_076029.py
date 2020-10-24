def lista_sufixos(string):
    lista=[]
    i=0
    while i < len(string):
        a=string[i::1]
        lista.append(a)
        i+=1
    return lista
    
        
