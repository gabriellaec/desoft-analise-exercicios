import math
from random import randint

def subtracao_de_listas (lista1,lista2):
    i = 0
    for e in lista1:
        excluiu = False
        while i<len(lista2) and not excluiu:
            if e == lista2[i]:
                del e
                excluiu = True
            i += 1
        i = 0
    return lista1 