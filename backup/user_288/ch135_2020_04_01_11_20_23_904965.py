lista = []
i = 0
def equaliza_imagem (k):
    while k > 0:
        lista[i] *= k
        if lista[i] > 0 and lista[i] < 255:
            print ('Cinza')
        elif lista[i] >= 255:
            print ('Branco')
        else:
            print ('Preto')
            
        i += 1
    return lista
    