def mais_populoso(dicionario):
    lista_compara = []
    for keys,dic in dicionario.items():
        total = sum(dic.values())
        lista_compara.append(total)
        print(lista_compara)

        for i in lista_compara:
            if i == max(lista_compara) and len(lista_compara)>1:
                return(keys)
            else: 
                continue