def alunos_impares(entrada):
    saida = []
    i=0
    while i<len(entrada):
        if i/2 != 0:
            saida.append(entrada[i])
        i+=1
    return saida