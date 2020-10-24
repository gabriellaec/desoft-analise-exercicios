def total_do_semestre_por_bairro(dicionario):
    total = {}
    for k,v in dicionario.items():
        soma = 0
        for i in range(len(v)):
            if i >= 6:
                soma += v[i]
        total[k] = soma
    return total