
def equaliza_imagem(lista_intensidades,k):
    for i in lista_intensidades:
        i = i*k
        if i > 255:
            i = 255
        print(lista_intensidades)
    