def equaliza_imagem (x,pixels):
    pixels = [10, 12, 100]
    lista2=[0]*len(pixels)
    x=10
    i=0
    while i<len(pixels):
        lista2[i]=pixels[i]*x
        if lista2[i]>225:
            lista2[i]=225
        i+=1
    return lista2
k=10
lista=[10,12,100]
resultado=equaliza_imagem(k,lista)
print (resultado)