
def equaliza_imagem(lista_intensidades,k):
    lista_nova = []
    for i in lista_intensidades:
        i_new = i*k
        if i_new > 255:
            i_new = 255
        lista_nova.append(i_new)
    return lista_nova    
    
 