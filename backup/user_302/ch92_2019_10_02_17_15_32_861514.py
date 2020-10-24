def simplifica_dict(dicionario):
    lista=[]
    for i in dicionario:
        if i in dicionario != dicionario[i]:
            lista.append(i)
            lista.append(dicionario[i])
    return lista
