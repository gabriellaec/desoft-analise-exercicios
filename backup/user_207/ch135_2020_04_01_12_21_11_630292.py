intensidades_de_pixels = [0, 10, 20, 30]
k = 3

def equaliza_imagem (intensidades_de_pixels, k):
    i=0
    imagem_equalizada = []
    while i<len(intensidades_de_pixels):
        imagem_equalizada.append (k* intensidades_de_pixels[i])
        i+=1

    return imagem_equalizada

