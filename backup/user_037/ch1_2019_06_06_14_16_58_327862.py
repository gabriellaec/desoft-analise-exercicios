def calcula_valor_devido(ve, m, tx):
    if m == 0:
        return ve
    i = 0
    while i < m:
        ve = ve*tx
        i += 1
        return ve
print(calcula_valor_devido(ve, m, tx))