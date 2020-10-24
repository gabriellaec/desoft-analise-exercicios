def equaliza_imagem (lista_pixels,k):
    i = 0
    while i < len(lista_pixels):
        lista_pixels[i] = lista_pixels[i] * k
        if lista_pixels > 255:
            lista_pixels = 255
            i = i + 1
        else:
            i = i + 1
    return lista_pixels