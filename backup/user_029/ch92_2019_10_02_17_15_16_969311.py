dic = {'a':'b','c':'b','b':'a'}
def simplifica_dict(dic):
    lista = []
    for k,v in dic.items():
        if k not in lista:
            lista.append(k)
        if v not in lista:
            lista.append(v)
    return lista
print(simplifica_dict(dic))