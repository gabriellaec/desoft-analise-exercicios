def faixa_notas(notas):
    lista = []
    soma = 0
    for i in range(len(notas)):
        if notas[i] > 5.0:
            soma = soma + 1
            lista.append(soma)
            
        elif notas[i] > 5.0 and notas[i] < 7.0:
            soma += 1
            lista.append(soma)
            
        elif notas[i] > 7.0:
            soma+=1
            lista.append(soma)

    return lista