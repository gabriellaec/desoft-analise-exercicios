lista_simples = []
def simplifica_dict(dicionario):
    lista_1 = dict.keys(dicionario)
    lista_2 = dict.values(dicionario)
    i = 0 
    while i < len(dicionario):
        if lista_1[i] != lista_2[i]:
            lista_simples.append(lista_1[i])
        else:
            lista_simples.append(lista_1[i])  and lista_simples.append(lista_2[i])
        i+= 1 
    return lista_simples