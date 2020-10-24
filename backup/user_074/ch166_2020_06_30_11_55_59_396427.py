def total_do_semestre_por_bairro(d):
    for x, y in d.items():
        y = d.values()
        i = 0
        while i <= len(y):
            i = 0 
            y[i] = x[5] + x[6] + x[7] + x[8] + x[9] + x[10] + x[11]
            i += 1
            append.dicio(y[i])
        return dicio