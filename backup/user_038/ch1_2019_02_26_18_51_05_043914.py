#Exercício 1
def calcula_valor_devido(valor, tempo, tx_juros):
    valor_final = valor*((1 + tx_juros/100)**tempo)
    print("O valor final do investimento será {0}".format(valor_final))
