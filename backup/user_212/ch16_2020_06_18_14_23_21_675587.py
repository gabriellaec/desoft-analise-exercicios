conta = float(input("qual o valor da sua conta"))

valor = conta + conta*0.1

arredonda = round(valor, 2)

texto = "Valor da conta com 10%: R${0}".format(arredonda)
print(texto)
