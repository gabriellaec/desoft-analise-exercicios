
def equaliza_imagem (intensidades,k):
    i=0
    while i<len(intensidades):
        intensidades[i]=intensidades[i]*k
        if intensidades[i]>255:
            intensidades[i] = 255
        i=i+1
        return intensidades
