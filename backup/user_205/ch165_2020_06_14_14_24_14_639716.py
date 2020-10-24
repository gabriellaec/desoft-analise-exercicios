def mais_populoso(dicionario):
    lista_compara = []
    for keys,dic in dicionario.items():
        total = sum(dic.values())
        lista_compara.append(total)

    if total == max(lista_compara):
        return(keys)