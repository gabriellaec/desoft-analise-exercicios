def calcula_norma(vetor):
    i = 0
    m = -100000000000
    for e in vetor:
        if e>m:
            m = e
    if vetor[i] < 0:
        vetor[i] = vetor[i]*(-1)
    soma = e + vetor[i]

            
