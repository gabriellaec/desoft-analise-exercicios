lista = []
i = 0
def equaliza_imagem (k):
    while k > 0 and lista[i] < 255:
        lista[i] *= k
        i += 1
    return lista
    