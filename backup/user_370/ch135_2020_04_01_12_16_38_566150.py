import numpy as np
def equaliza_imagem(lista,k):
    i=True
    i=0
    while i:
        pixels= np.array([lista]*k)
        if pixels[i] > 255:
            print(')