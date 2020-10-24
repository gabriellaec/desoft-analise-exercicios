def subtracao_de_listas(lista1, lista2):
lista1=[1,2,3,4]
lista2=[2,3,5]
i=0
while i in lista1:
    if lista1[i] - lista2[i] == 0:
        del lista2[i]
    return lista2
        