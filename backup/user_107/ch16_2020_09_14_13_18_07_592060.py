valor = float(input('Qual o valor da conta?'))
gorjeta = valor * 10/100 # 10% do valor

valor += gorjeta

print('Valor da conta com 10%: R$ {0:.2f}'.format(valor))