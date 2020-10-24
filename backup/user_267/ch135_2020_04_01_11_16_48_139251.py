lista_nova = []
def equaliza_imagem(lista_intensidades,k):
    for i in lista_intensidades:
        i = i*k
        lista_nova.append(i)
        if i > 255:
            i = 255
        print(lista_nova)
    