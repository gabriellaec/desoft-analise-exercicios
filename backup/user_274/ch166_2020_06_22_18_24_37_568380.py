def total_do_semestre_por_bairro(gastos):
    new = {}
    for i,j in gastos.items():
        s = 0
        c = 0
        for a in j:
            if c >= 5:
                s = s + a
            c = c + 1
        new[i] = s
    return new