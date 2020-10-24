def traduz(lista,dic):
    lista_traduzida = []
    for i in lista:
        if i in dic:
            lista_traduzida.append(dic[i])
            
    return lista_traduzida 
            