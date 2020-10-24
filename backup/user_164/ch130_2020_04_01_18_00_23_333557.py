def monta_mala (pesos_em_kg):
    resultado = []
    a = 0
    for i in range (len(pesos_em_kg)):
        a += pesos_em_kg[i]
        if a > 23:
            break 
        resultado.append(pesos_em_kg[i])
    return resultado