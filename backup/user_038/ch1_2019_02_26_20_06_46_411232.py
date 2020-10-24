#Exercício 1
def calcula_valor_devido(valor, tempo, tx_juros):
    valor_final = valor*((1 + tx_juros/100)**tempo)
    return valor_final