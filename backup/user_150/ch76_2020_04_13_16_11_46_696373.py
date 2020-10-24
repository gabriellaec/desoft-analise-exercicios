def aniversariantes_de_setembro(nomes):
    aniversario_em_setembro = {}
    i = 0
    for k, v in nomes.items():
        if v[3] == '0' and v[4] == '9':
            aniversario_em_setembro[k] = v
            i += 1
    return aniversario_em_setembro