def faixa_notas(notas):
    lista = []
    soma = 0
    for i in range(len(notas)):
        if notas[i] > 5.0:
            soma = soma + 1
            lista.insert(0,soma)
            
        elif notas[i] > 5.0 and notas[i] < 7.0:
            soma += 1
            lista.insert(1,soma)
            
        elif notas[i] > 7.0:
            soma+=1
            lista.insert(2,soma)

    return lista