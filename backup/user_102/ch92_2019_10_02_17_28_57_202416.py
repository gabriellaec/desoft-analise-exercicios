def simplifica_dict(dicionario):
    listanova = []
    lista_keys = list(dicionario.keys())
    lista_values = list(dicionario.values())
    for i in lista_keys:
        if i not in listanova:
            listanova.append(i)
    for e in lista_values:
        if e not in listanova:
            listanova.append(e)
    print(listanova)
