from math import*
def calcula_norma(lista_vetor):
    value = 0
    for dimensao in lista_vetor:
        value += dimensao**2
    norma = sqrt(value)
    return norma