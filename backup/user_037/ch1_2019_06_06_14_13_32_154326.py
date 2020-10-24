def calcula_valor_devido(ve, m, tx):
    if m == 0:
        return ve
    i = 0
    while i < m:
        valor_devido = ve*tx
        i += 1
        return valor_devido
    