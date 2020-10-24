def junta_listas (x):
    lista=[]
    
    for termo in x:
        i=0
        while i<len(termo):
            lista.append (termo[i])
            i+=1
    return lista