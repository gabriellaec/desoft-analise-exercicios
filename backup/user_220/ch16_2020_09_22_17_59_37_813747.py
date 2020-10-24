numero = float(input("Qual o valor da conta? "))

def calculo(numero):
    novo = (10/100 * numero) + numero
    return novo

novo = calculo(numero)

print("Valor da conta com 10%: R$ {0:.2f}".format(novo))