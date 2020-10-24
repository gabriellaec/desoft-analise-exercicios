def agrupa_por_idade (dic1):
    # chaves sao nomes (strings)
    # valores sao idades
    nomes_c = []
    nomes_a = []
    nomes_ad = []
    nomes_i = []

    dic2 = {
        "criança": nomes_c,
        "adolescente": nomes_a,
        "adulto": nomes_ad,
        "idoso": nomes_i
    }
    #chaves sao faixas etarias
    #valores sao listas com os nomes das pessoas naquela faixa
    for k,v in dic1.items():
        if v <= 11:
            nomes_c.append (k)
        elif v>11 and v<18:
            nomes_a.append(k)
        elif v>17 and v<60:
            nomes_ad.append(k)
        else:
            nomes_i.append(k)
    return dic2