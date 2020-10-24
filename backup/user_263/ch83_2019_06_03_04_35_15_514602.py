def medias_por_inicial(entrada):
    alunos = entrada
    saida = {}
    n = 1
    for k,v in alunos:
        if k[0] not in saida:
            saida[k[0]] = v
        else:
            saida[k[0]] = ((saida[k[0]]*n) + v)/(n+1)
            n += 1 
    return saida
            