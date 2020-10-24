def interseccao_chaves(dicionario1,dicionario2):
    dicionario1={'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dicionario2={'e':5,'f':6,'g':7,'h':8}
    lista=[]
    
    for k,v in dicionario1.items():
        lista.append(k)
    for k,v in dicionario2.items():
        lista.append(k)

    return lista
