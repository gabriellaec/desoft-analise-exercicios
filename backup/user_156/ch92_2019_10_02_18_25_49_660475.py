def simplifica_dict(dicionario):
    list_key_value = [ [k,v] for k, v in dicionario.items()] ]
    lista2 = []
    for i in list_key_value:
        if i not in lista2:
            lista2.append(i)
    lista2.sort()
    return lista2





            
            