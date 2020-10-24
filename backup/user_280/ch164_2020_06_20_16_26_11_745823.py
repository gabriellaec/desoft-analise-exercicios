def traduz(lista_ing, dic_traducoes):
    i = 0
    lista_port = []
    while i < len(lista_ing):
        for word, palavra in dic_traducoes.items():
            if word == lista_ing[i]:
                lista_port.append(palavra)
        i+=1
    return lista_port