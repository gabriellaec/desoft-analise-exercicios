def medias_por_inicial(dicnotas):
    letra_notas = {}
    contador = 1
    for nome in dicnotas:
        prim_let = nome[0]
        for nota in dicnotas[nome]:
            if prim_let not in letra_notas:
                letra_notas[prim_let] = nota
            else:
                letra_notas[prim_let] *= contador
                contador += 1
                letra_notas[prim_let] = (letra_notas[prim_let]+nota)/contador
    return letra_notas
                