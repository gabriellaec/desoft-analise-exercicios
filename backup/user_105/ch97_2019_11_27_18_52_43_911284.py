def total_do_semestre_por_bairro(dicio):
    dicio1 = {}
    cont = 0
    soma = 0
    x = dicio.values()

    for i in dicio:
        x = dicio[i]
        cont += 1
        if cont > 6:
            soma += i