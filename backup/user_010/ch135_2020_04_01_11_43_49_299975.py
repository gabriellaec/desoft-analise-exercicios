def equaliza_imagem (pixels,x):
    
    lista2=[0]*len(pixels)
    
    i=0
    while i<len(pixels):
        lista2[i]=pixels[i]*x
        if lista2[i]>255:
            lista2[i]=255
        i+=1
    return lista2
