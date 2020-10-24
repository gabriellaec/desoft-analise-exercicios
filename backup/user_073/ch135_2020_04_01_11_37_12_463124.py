def equaliza_imagem(cores, k):
    for i in range(len(cores)):
        cores[i]=cores[i]*k
        if (cores[i]>255):
            cores[i]=255
    return cores