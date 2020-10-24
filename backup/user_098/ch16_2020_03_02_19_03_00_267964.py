valor = float(input("Qual o valor da conta?"))

valor_final = 1.10*valor

print("Valor da conta com 10%: R$ {0:.2f}".format(round(valor_final,2)))