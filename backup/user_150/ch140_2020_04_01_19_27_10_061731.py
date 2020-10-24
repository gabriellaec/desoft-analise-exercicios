def faixa_notas(listanotas):
    listaclassificacao = []
    listanotas_counter = 0
    quantidademenorque5 = []
    quantidadeentre5e7 = []
    quantidademaiorque7 = []
    while listanotas_counter < len(listanotas):
        if listanotas[listanotas_counter] < 5:
            quantidademenorque5.append(listanotas[listanotas_counter])
            listaclassificacao.append(len(quantidademenorque5))
        elif listanotas[listanotas_counter] >= 5 and listanotas[listanotas_counter] <= 7:
            quantidadeentre5e7.append(listanotas[listanotas_counter])
            listaclassificacao.append(len(quantidadeentre5e7))
        else:
            quantidademaiorque7.append(listanotas[listanotas_counter])
            listaclassificacao.append(len(quantidademaiorque7))
        listanotas_counter += 1