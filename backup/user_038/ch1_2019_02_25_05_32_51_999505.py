#Exercício 1
def calcula_valor_devido(valor, tempo, tx_juros):
    valor_final = valor*((1 + tx_juros/100)**tempo)
    print("O valor final do investimento será {0}".format(valor_final))
v = float(input("Quanto deseja aplicar? "))
n = int(input("Por quanto tempo? "))
tx = float(input("Qual a taxa de juros em porcentagem? "))
calcula_valor_devido(v, n, tx)