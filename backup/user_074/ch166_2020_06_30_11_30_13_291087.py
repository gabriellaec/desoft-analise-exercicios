def total_do_semestre_por_bairro(d):
    for x, y in d.items():
        y= d.values()
        n = 5
        if n <= 11:
            y = y[n] + y[n-1]
            n +=1
        append.dicio = {y:x}

        return dicio