def interseccao_chaves(dicionario1,dicionario2):
    dicionario1={'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dicionario2={'e':5,'f':6,'g':7,'h':8}
    lista=[]
    dicionario1.update(dicionario2)
    for k,v in dicionario1.items():
        lista.append(k)

    return lista

