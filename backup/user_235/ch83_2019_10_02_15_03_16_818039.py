Entrada= {'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}

Saída_comparação= {'A': 6, 'F': 9.5, 'R': 8}

def medias_por_inicial(x):
    acumulador = {}
    somas = {}    
    for i in x:
        if i[0] in acumulador:
            acumulador[i[0]] += 1
            somas[i[0]] += x[i]
        else:
            acumulador[i[0]] = 1
            somas[i[0]] = x[i]
    saida = {}
    for i in acumulador:
        saida[i] = somas[i]/acumulador[i]
    return saida