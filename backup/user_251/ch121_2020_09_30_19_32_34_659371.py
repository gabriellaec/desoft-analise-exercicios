from collections import Counter
def subtracao_de_listas(lista_1, lista_2):
    a = Counter(lista_1)
    b = Counter(lista_2)
    c = a - b
    return list(c.elements())
