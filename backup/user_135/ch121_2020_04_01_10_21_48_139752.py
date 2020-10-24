indice1 = 0
indice2 = 0

def subtracao_de_listas(lista1,lista2):
    lista3 = []
    while indice1 < int(len(lista1)):
        if lista1[indice1] != lista2[indice2]:
            lista3.append(lista1[indice1]
            indice1 += 1
            indice2 = 0
        else:
            if indice2 == int(len(lista2)):
                indice2 = 0
            else:
                indice2 += 1