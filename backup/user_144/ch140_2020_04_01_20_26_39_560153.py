def faixa_notas(notas):
    lista = []
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(len(notas)):
        if notas[i] < 5:
            s1 += 1
            lista.append(s1)
            
        elif notas[i] > 5 and notas[i] < 7:
            s2 += 1
            lista.append(s2)
            
        elif notas[i] > 7:
            s3 += 1
            lista.append(s3)
            
    return lista