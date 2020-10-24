def total_do_semestre_por_bairro(d):
    for x, y in d.items():
        y = d.values()
        i = 0
        while i <= len(y):
            for n in range(list(x)):
                i = 0 
                n = 5
                if n <= 11:
                    y[i] = x[n] + x[n-1]
                    n +=1
                    i += 1
                    append.dicio = {}
        return dicio