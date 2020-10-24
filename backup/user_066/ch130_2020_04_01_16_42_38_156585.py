def monta_mala(pesos):
    peso_total = 0
    pesos_aceitaveis = []
    for i in pesos:
        peso_total += i
        if peso_total>23:
            break
        else:
            pesos_aceitaveis.append(i)
    return pesos_aceitaveis
            