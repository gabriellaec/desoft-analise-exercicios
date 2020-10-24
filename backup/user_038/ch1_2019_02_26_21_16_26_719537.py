def calcula_valor_devido(valor, tempo, tx_juros):
    valor_final = valor*((1 + tx_juros)**tempo)
    return valor_final