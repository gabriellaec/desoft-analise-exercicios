def calcula_valor_devido(ve, ndm, tdj):
    montante = ve*(1 + (tdj/100))**ndm
    return montante
