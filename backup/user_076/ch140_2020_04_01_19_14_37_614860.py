def faixa_notas(notas):
    contador = 0 
    notas_menores_que_5 = 0
    notas_entre_5_e_7 = 0
    notas_maiores_que_7 = 0
    while contador < len(notas):
        if notas[contador] < 5:
            notas_menores_que_5 +=1
        if 5 <= notas[contador] <=7:
            notas_entre_5_e_7 += 1
        if notas[contador] > 7:
            notas_maiores_que_7 +=1
        contador += 1
    lista = []
    lista[0] = notas_menores_que_5
    lista[1] = notas_entre_5_e_7
    lista[2] = notas_maiores_que_7
    return lista