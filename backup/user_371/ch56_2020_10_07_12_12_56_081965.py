def calcula_norma(vetor):
    print(vetor)
    i=0
    while i<len(vetor):
        if vetor[i]<0:
            vetor[i]=vetor[i]*-1
            i+=1
        else:
            i+=1
    return vetor