def interseccao_chaves(dicionario1,dicionario2):
    lista=[]
    for i in dicionario1.keys():
        lista.append(i)
        
    for e in dicionario2.keys():
        lista.append(e)
        
    return lista
