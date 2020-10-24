lista=[]
def simplifica_dict(dici):
    for k in dici.key():
        if k not in lista:
            lista.append(k)
    for v in dici.values():
        if v not in lista:
            lista.append(v)
    return lista
