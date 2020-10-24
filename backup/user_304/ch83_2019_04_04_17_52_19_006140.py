def medias_por_inicial(notas):
    inicial={}
    for nome,valor in notas.items():
        x=nome[0]
        inicial[x]=valor
    return inicial