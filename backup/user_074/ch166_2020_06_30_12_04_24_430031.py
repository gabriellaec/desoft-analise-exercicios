def total_do_semestre_por_bairro(d):
    for x, y in d.items():
        y = d.values()
        i = 0
        while i <= len(y):
            i = 0 
            del(x[:4])
            x[0][i] = x[5] + x[6] + x[7] + x[8] + x[9] + x[10] + x[11]
            dicio = {y[i]: x[0][i]}
            i += 1
        return dicio