def interseccao_chaves(dic1,dic2):
    interseccao=[]
    lista_valores=[]
    for i in dic2.values:
        lista_valores.append(i)
    for k in dic1:
        if dic1[k] in lista.valores:
            interseccao.append(dic1[k])
    return interseccao
            
    