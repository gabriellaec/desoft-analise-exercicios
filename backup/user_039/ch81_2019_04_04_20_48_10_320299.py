def interseccao_valores(dicionario1,dicionario2):
    lista=[]
    interseccao=[]
    
    for e in dicionario2.values():
        lista.append(e)
    for i in dicionario1.values():
        if dicionario1[i] in lista:
            interseccao.append(dicionario1[i])
                
    return lista
                