lista1 = [4,1,2,5,3,6]
lista2 = [4,5,6,7,8,9]
def subtracao_de_listas(lista1,lista2):
    t = 0
    while t<len(lista1):
        if lista1[t] in lista2:
            del lista1[t]
            t+=1
        else:
            t+=1
    return

print(lista1)