def total_do_semestre_por_bairro (d):
    dici = {}
    for j, i in d.items():
        s = 0
        for c in range(len(i)):
            if c >= 6:
                s += i[c]
        dici[j] = s
    return dici        
            