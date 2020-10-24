def calcula_valor_devido(ve, m, tx):
    i = 0
    if m == 0:
        return ve
    if tx == 0:
        return ve
    if ve == 0:
        return ve
    
    else:
        while i < m:
            ve = ve + ve*tx
            i += 1
        return ve
    
