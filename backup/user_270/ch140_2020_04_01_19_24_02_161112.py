def faixa_notas(l):
    i = 0
    q5 = 0
    q5_7 = 0
    q7 = 0
    notas = []
    while i < len(l):
        if l[i] < 5:
            q5 += 1
        elif l[i] >= 5 and l[i] <= 7 :
            q5_7 += 1
        elif l[i] > 7:
            q += 1
        i += 1
    notas.append[q5]
    notas.append[q5_7]
    notas.append[q7]
    return notas
         
        