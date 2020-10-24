def traduz(lista,dic):
    traducao = []
    for i in lista:
        for palavara in dic:
            if lista[i] == palavara:
                traducao.append(dic[palavara])
    return traducao