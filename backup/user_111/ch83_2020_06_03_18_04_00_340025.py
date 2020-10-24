def medias_por_inicial(dicionario_notas):
    dicionariosomas={}
    dicionarioconta={}
    for nome,notas in dicionario_notas.items():
        primeiraletra=nome[0]
        if primeiraletra not in dicionariosomas:
            dicionariosomas[primeiraletra]=0
            dicionarioconta[primeiraletra]=0
        dicionariosomas[primeiraletra]+=notas
        dicionarioconta[primeiraletra]+=1
    for primeiraletra in dicionariosomas:
        dicionariosomas[primeiraletra]/=dicionarioconta[primeiraletra]
    return dicionariosomas