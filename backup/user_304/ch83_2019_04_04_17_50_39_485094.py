def media_por_inicial(notas):
    inicial={}
    for nome,valor in notas.items():
        x=nome[0]
        inicial[nome[0]]=valor
    return inicial