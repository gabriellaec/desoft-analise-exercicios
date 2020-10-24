def calcula_valor_devido(ve, m, tx):
    i = 0
    while i < m:
        ve = ve*tx
        i += 1
        return ve