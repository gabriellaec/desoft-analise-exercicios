def calcula_valor_devido(ve,m,tj):
    juros=ve*(((1-tj)**m)-1)
    total=juros+ve
    return total