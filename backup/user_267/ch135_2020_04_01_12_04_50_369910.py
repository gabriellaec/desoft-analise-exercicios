
def equaliza_imagem(lista_intensidades,k):
    lista_nova = []
        for i in lista_intensidades:
            i = i*k
            if i > 255:
                i = 255
                lista_nova.append(i)
            else:
                lista_nova.append(i)
            print(lista_nova)