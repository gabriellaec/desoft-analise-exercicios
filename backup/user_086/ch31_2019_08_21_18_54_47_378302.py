valor=float(input('Qual o valor da casa a ser comprado? '))
salario=float(input('Qual o seu salário? '))
anos=float(input('Durante quanto tempo deseja pagar? '))
if valor/(anos*12)>0.3*salario:
	print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')