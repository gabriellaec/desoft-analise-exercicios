def faixa_notas(lista):
    abaixo=0
    media=0
    acima=0
    for nota in lista:
        if nota<5:
            abaixo+=1
        elif nota<=7:
            media+=1
        else:
            acima+=1
    resultados=[abaixo,media,acima]
    return resultados