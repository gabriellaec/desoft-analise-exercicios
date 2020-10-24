def medias_por_inicial(nome_nota):
    inicial = {}
    ocorrencia = 1
    s = inicial[nome[0]]
    for nome,nota in nome_nota.items():
        if not nome[0] in inicial:
            inicial[nome[0]] = nota
        else:
            ocorrencia += 1
            s += nome_nota[nome] 
            inicial[nome[0]] = s/ocorrencia
    return inicial