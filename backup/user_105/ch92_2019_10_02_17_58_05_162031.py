def simplifica_dict(dicio1):
    lista_simplificada = []
    x = dicio1.values()
    for i in dicio1:
        if i not in lista_simplificada:
            lista_simplificada.append(i)
    for n in x:
        if n not in lista_simplificada:
            lista_simplificada.append(n)
        
    return lista_simplificada