def total_do_semestre_por_bairro(gastos):
    new = {}
    for i in gastos:
        s = 0
        c = 0
        for j in i:
            s = s + j
            c = c + 1
            if c = 5:
                break
        new[i] = s
    return new