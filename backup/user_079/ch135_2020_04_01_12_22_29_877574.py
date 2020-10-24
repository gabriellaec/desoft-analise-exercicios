def equaliza_imagem(x):
    i=0
    z=[]
    while i<len(x):
        y=x[i]*k
        if y >= 255:
            y=255
        z.append(y)
        i+=1
    return z