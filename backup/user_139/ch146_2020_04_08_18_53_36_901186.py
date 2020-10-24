def conta_ocorrencias ('lista'):
    dic = {}
    for palavra in lista:
        if not palavra in dic:
            dic [palavra] = 1
        else:
            dic [palavra] += 1
    return dic