def faixa_notas(listanotas):
    listaclassificacao = []
    listanotas_counter = 0
    while listanotas_counter < len(listanotas):
        if listanotas[listanotas_counter] < 5:
            listaclassificacao.append(len(listanotas[listanotas_counter]))
        elif listanotas[listanotas_counter] >= 5 and listanotas[listanotas_counter] <= 7:
            listaclassificacao.append(len(listanotas[listanotas_counter]))
        else:
            listaclassificacao.append(len(listanotas[listanotas_counter]))
        listanotas_counter += 1
    return listaclassificacao