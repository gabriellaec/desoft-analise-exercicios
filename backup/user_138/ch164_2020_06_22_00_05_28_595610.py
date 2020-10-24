def traduz (lista_ingles,dict_traducao):
    lista = []
    for i in dict_traducao:
        for n in lista_ingles:
            if n == i:
                lista.append(dict_traducao[i])
    return lista