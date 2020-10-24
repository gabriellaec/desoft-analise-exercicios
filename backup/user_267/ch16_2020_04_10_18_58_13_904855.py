pergunta_conta=float(input('Qual o valor da conta? '))
valor = pergunta_conta*1.1
print(valor)
print("Valor da conta com 10%: R$ {0}.{1}{2}".format(valor[0],valor[1],valor[2]))