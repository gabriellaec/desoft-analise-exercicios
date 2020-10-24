def calcula_valor_devido(val, mes, tax):
    return ( val * ( (1+tax) ** mes ) )