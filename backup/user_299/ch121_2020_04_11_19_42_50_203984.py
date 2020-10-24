import math
from random import randint

def subtracao_de_listas (lista1,lista2):
    i = 0
    for j,e in enumerate(lista1):
        excluiu = False
        while i<len(lista2) and not excluiu:
            if e == lista2[i]:
                del lista1[j]
                excluiu = True
            i += 1
        i = 0
    return lista1 

lista1 = [2, 7, 3.1, 'banana']
lista2 = [2, 'banana', 'carro']

print(subtracao_de_listas(lista1,lista2))