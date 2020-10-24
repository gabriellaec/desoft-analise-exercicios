def calcula_valor_devido (valor, número, taxa):
    y = valor * (1 + taxa) ** número
    return y