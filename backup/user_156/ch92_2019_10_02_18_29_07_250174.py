def simplifica_dict(dicionario):
    lista = []
    for k,v in dicionario.items():
        lista.append(k)
        lista.append(v)
        
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    lista2.sort()
    return lista2







            
            