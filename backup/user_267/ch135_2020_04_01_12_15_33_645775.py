
def equaliza_imagem(lista_intensidades,k):
    lista_nova = []
    for i in lista_intensidades:
        if i not in lista_nova:
            i_new = i*k
            lista_nova.append(i_new)
    return lista_nova    
    
 