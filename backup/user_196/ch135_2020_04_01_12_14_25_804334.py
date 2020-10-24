def equaliza_imagem(p,k):
    listafinal = []
    i=0
    while i < (len(p)):
        j = p[i]*k
        i+=1
        if j > 255:
            listafinal.append(255)
        else:
            listafinal.append(j)
    return listafinal