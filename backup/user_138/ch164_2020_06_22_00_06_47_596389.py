def traduz (lista_ingles,dict_traducao):
    lista = []
    for n in lista_ingles:
        for i in dict_traducao:
            if n == i:
                lista.append(dict_traducao[i])
    return lista