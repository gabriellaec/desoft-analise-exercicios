intensidades_de_pixels = [0, 10, 20, 30]
k = 3

def equaliza_imagem (intensidades_de_pixels, k):
    i=0
    imagem_equalizada = [0]*len(intensidades_de_pixels)
    while i<len(intensidades_de_pixels):
        imagem_equalizada[i] = (k* intensidades_de_pixels[i])
        if equaliza_imagem[i] >= 255:
            equaliza_imagem[i] = 255
        i+=1

    return imagem_equalizada