def medias_por_inicial(notas):
    media = dict()
    c = 0
    for nome, nota in notas.items():
        if not nome[0] in media:
            media[nome[0]] = nota
            c += 1
        else:
            media[nome[0]] = sum(nota)/c
            
    return media
            
        
            
        
    