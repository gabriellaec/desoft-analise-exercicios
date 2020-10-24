def simplifica_dict(dicionario):
    lista_simplificada = []
    for chave, valor in dicionario.items():
        lista_simplificada.append(chave)
        lista_simplificada.append(valor)

    dic_lista_simplificada = list(dict.fromkeys(lista_simplificada))

    lista_simplificada = list(dic_lista_simplificada)

    return lista_simplificada

d = {'a': 'b', 'c':'d'}

print(simplifica_dict(d))