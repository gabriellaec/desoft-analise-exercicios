def bairro_mais_custoso(gastos):
    m = ""
    e = 0
    for i,j in gastos.items():
        s = 0
        c = 0
        for a in j:
            if c >= 6:
                s = s + a
            c = c + 1
        if s > e:
            e = s
            m = i
    return m