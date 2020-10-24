def faixa_notas(lnotas):
    m = len(lnotas)
    i = 0
    listaf = []
    p1 = 0
    p2 = 0
    p3 = 0
    while i < m:
        nota = lnotas[i]
        i += 1
        if nota < 5:
            p1 += 1 
        elif nota >= 5 and nota <= 7:
            p2 += 1 
        else:
            p3 += 1
    listaf.append(p1)
    listaf.append(p2)
    listaf.append(p3)
    return(listaf)
    