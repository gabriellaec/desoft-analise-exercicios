def faixa_notas(notas):
    i = 0
    menor_que_5 = 0
    entre_5_e_7 = 0 
    maior_que_7 = 0 
    while i < len(notas):
        if notas[i] < 5:
            menor_que_5 += 1 
        elif notas[i] >= 5 and notas[i] <= 7: 
            entre_5_e_7 +=1
        else:
            maior_que_7 +=1
        i+=1
    lista_final = [menor_que_5, entre_5_e_7, maior_que_7]
    return lista_final
