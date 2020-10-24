conta = input(float("qual o valor da sua conta"))

valor = conta + conta*0.1

arredonda = round(valor, 2)

print( "Valor da conta com 10%: R$" + float(arredonda))
