def faixa_notas(lista_notas):
    notas_baixas = 0
    notas_medianas = 0
    notas_altas = 0
    for notas in lista_notas:
        if notas_baixas < 5:
            notas_baixas = notas_baixas + 1
        elif notas >=5 and notas <=7:
            notas_medianas = notas_medianas + 1
        elif notas > 7:
            notas_altas = notas_altas + 1
    lista_notas_final = [notas_baixas, notas_medianas, notas_altas]
    return lista_notas_final