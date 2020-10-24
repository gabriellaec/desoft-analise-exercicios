def medias_por_inicial(dicionario_notas):
    dicionariosomas={}
    for nome,notas in dicionario_notas.items():
        primeiraletra=nome[0]
        dicionariosomas[primeiroletra]+=notas
    return dicionariosomas
    
    