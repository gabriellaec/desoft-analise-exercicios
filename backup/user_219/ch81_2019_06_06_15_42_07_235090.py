def interseccao_valores(dic1,dic2):
    lista1= []
    lista2=[]
    saida=[]
    for chaves,valores1 in dic 1:
        lista1.append(valores1)
    for chave,valores2 in dic2:
        lista2.append(valores2)
    for i in lista1:
        if i in lista2:
            saida.append(i)
    return saida