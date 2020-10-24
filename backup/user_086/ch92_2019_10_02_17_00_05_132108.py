def simplifica_dict(dic):
    lista=[]
    for i in dic:
        if not dic[i] in lista:
            lista.append(dic[i])
        if not i in lista:
            lista.append(i)
    return lista