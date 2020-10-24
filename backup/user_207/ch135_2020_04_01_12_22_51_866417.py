def equaliza_imagem (intensidades_de_pixels, k):
    i=0
    imagem_equalizada = []
    while i<len(intensidades_de_pixels):
        imagem_equalizada.append (k* intensidades_de_pixels[i])
        if equaliza_imagem[i] >= 255:
            equaliza_imagem[i] = 255
        i+=1

    return imagem_equalizada

