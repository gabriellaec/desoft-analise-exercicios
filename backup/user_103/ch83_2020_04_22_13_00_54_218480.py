def medias_por_inicial(dicionario_notas):
    dicionariosomas={}
    for nome,notas in dicionario_notas.items():
        primeiraletra=nome[0]
        if primeiraletra not in dicionariosomas:
            dicionariosomas[primeiraletra]=0
        dicionariosomas[primeiraletra]+=notas
    print (dicionariosomas)
    
    