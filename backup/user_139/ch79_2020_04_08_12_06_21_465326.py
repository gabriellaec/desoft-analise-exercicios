lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
def monta_dicionario (x, y):
    dic = {}
    for i in range(len(x)):
        dic[x[i]] = y[i]
    return dic
print (monta_dicionario(lista1, lista2))