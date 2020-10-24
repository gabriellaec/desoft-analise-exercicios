def medias_por_inicial(notas):
    dici = {}
    soma = 0
    for nome,nota in notas.items():
        inicial = nome[0]
        if inicial in dici:
            soma += nota
            dici[str(inicial)] = soma/2
        else:
            dici[str(inicial)] = nota
            soma = nota
    return dici
            