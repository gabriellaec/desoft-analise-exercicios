#Programa que pergunta ao usuário o valor da conta do restaurante e imprime: "Valor da conta com 10%: R$ X.YZ", onde X.YZ é um numero com exatamente duas casas decimais

valor = float (input ('Valor da conta: '))
valor_com_10 = valor * 1.1
print ('Valor da conta com 10% R$ {0:.2f} '.format(valor_com_10))


