valordaconta = float(input('qual o valor da conta'))
contacomservico = (valordaconta/10)+valordaconta
y = round(contacomservico, 2)
print('Valor da conta com 10%: R${}'.format(y))