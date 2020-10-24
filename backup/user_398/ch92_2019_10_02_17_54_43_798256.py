def simplifica_dict(dicionario):
    lista=[]
    for i in dicionario:
        if i not in lista:
            lista.append(i)
    for e in dicionario.values():
        if e not in lista:
            lista.append(e)
    return lista
