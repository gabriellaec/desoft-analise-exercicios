def calcula_media(ano):
    numero = 0
    soma = 0
    for turma in ano:
        for media in turma.values():
            soma += media
            numero += 1
            
    mediafinal = soma/numero
    return mediafinal