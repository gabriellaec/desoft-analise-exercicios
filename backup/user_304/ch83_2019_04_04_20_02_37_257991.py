def medias_por_inicial(notas):
    inicial={}
    for nome,valor in notas.items():
        if nome[0] not in inicial:
            inicial[nome[0]]=valor
        else:
            valor=(valor+valor)/2
            inicial[nome[0]]=valor
    return inicial
