def faixa_notas(entrada):
    i = 0
    menor5 = 0
    entre5e7 = 0
    maior7 = 0
    saida = []
    while i < len(entrada):
        if entrada[i] > 7 and entrada[i] < 11:
            maior7 +=1
        elif entrada[i] >= 5 and entrada[i] <= 7:
            entre5e7 += 1
        elif entrada[i] < 5 and entrada[i] >= 0:
            menor5 +=1
        
        i += 1
    saida.append(menor5)
    saida.append(entre5e7)
    saida.append(maior7)
    
    return saida