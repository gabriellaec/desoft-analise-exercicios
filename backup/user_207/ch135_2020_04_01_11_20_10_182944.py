def equaliza_imagem (intensidade_de_pixels, k):
    i=0
    while i<len(intensidade_de_pixels):
        imagem_equalizada[i] = k*intensidade_de_pixels[i]
    if imagem_equalizada[i] > 255:
        imagem_equalizada[i] = 255
    i +=1
    return imagem_equalizada