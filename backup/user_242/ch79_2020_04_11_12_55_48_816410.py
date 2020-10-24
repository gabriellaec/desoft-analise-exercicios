lista1 = ['a', 'b','c', 'd']
lista2 = [1,2,3,4]
i=0
dict={}
def monta_dicionario(lista1,lista2):
    dict[lista1[i]] = lista2[i]
    i+=1
print(dict)