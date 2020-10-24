def equaliza_imagem(x,k):
    i=0
    z=[]
    while i<len(x):
        y=x[i]*k
        if y >= 255:
            y=255
        z.append(y)
    print(z)