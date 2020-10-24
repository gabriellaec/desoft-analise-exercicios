def traduz (lista_ing, ing_para_port):
    lista_port = []
    i = 0
    while i < len(lista_ing):
        for palavra_ing in ing_para_port.keys():
            if palavra_ing == lista_ing[i]:
                lista_port.append(ing_para_port[palavra_ing])
        i += 1
    return lista_port