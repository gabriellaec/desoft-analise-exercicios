def traduz(lista_ing,dic):
    traduzida=[]
    for i in lista_ing:
        for k,v in dic.items():
            if i == k:
                traduzida.append(v)
    return traduzida
