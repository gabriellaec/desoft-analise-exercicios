import numpy as np
def total_do_semestre_por_bairro(t):
    t = dict()
    lista_numeros = np.arange(0,12) 
    for i in range(1,13):
        t[(f'Bairro{i}')] = lista_numeros
        for j in range(len(lista_numeros)):
            total = sum(lista_numeros[j])
            t2 = dict()
            t2[(f'Bairro{i}')] = total
            return t2