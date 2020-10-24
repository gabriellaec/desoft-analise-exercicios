valor_da_casa = float(input('qual eh o valor da casa a comprar? '))
salario = float(input('qual eh o seu salario? '))
anos = float(input('em quantos anos vc vai pagar? '))
if (valor_da_casa)/(anos*12) <= salario*0.3:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')
