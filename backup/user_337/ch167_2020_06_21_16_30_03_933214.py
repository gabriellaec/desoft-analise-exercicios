
def bairro_mais_custoso(dicionario):
    dic = {}
    for bairro in dicionario:
        gasto = 0
        lista = dicionario[bairro]
        for valor in lista[6:12]:
            gasto += valor
        dic[bairro] = gasto
    b = 0
    for i in dic.values():
        if i>b:
            i = b
    return b