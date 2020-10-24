def interseccao_de_valores(dict1, dict2):
    interseccao=[]
    valores=[]
    for palavra1 in dict1:
        valores.append(palavra1)
    for palavra2 in dict2:
        if palavra2 in valores:
            interseccao.append(palavra2)
    return interseccao