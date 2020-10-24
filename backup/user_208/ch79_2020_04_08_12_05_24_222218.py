lista1 = ["A","B","C","D","E"]
lista2 = [1,2,3,4,5]
def monta_dicionario (letra,numero):
    dic = {}
    for i in range(len(letra)):
        dic[letra[i]] = numero[i]
    return dic
print (monta_dicionario(lista1,lista2))
    
    