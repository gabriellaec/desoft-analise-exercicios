def simplifica_dict(d):
    lista = []
    for k,v in d.items():
        if k not in lista:
            lista.append(k)
        if v not in lista:
            lista.append(v)
    return lista