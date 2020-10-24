valor_da_casa = float(input('qual eh o valor da casa a comprar? '))
salario = float(input('qual eh o seu salario? '))
anos = float(input('em quantos anos vc vai pagar? '))
if (valor_da_casa*12)/anos <= salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')
