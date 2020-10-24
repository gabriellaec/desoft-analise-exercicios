def estado (dic):
    estado_populacao = {}
    for i,n in dic.items():
        h = []
        for x in n.values():
            h.append(x)
        z = 0
        for y in h:
            z += y
        estado_populacao[i] = z
    hab_Est = 0
    mais_pop = ''
    for i,n in estado_populacao.items():
        if n > hab_Est:
            hab_Est = n
            mais_pop = i
    return mais_pop
