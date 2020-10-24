def medias_por_inicial(notas_individuais):
    soma_notas_iniciais = {}
    quantidade_por_inicial = {}
    medias = {}
    for nome, nota in notas_individuais.items():
        if nome[0] not in soma_notas_iniciais.keys():
            soma_notas_iniciais[nome[0]] = nota
            quantidade_por_inicial[nome[0]] = 1
        else:
            soma_notas_iniciais[nome[0]] += nota
            quantidade_por_inicial[nome[0]] += 1
    for nome, soma_notas in soma_notas_iniciais.items():
        medias[nome] = soma_notas_iniciais[nome]/quantidade_por_inicial[nome]
    return medias