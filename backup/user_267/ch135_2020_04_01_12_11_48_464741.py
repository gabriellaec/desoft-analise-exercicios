
def equaliza_imagem(lista_intensidades,k):
    lista_nova = []
    elementos_lista = len(lista_intensidades)
    i = 0
    while i<elementos_lista - 1:
        lista_intensidade[i] = lista_intensidade[i]*k
        lista_nova.append(lista_intensidade[i])
        i += 1
        
    for i in lista_intensidades:
        i = i*k
        if i > 255:
            i = 255
            lista_nova.append(i)
        else:
            lista_nova.append(i)
        print(lista_nova)