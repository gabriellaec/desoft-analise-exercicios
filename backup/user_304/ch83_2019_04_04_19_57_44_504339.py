def medias_por_inicial(notas):
    inicial={}
    for nome,valor in notas.items():
        inicial[nome[0]]=valor
    return inicial
