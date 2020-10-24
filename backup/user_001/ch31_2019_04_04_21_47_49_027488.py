desejo = int(input('Quanto custa? '))
salario = int(input('Seu salário: '))
anos = int(input('Quantos anos para pagar? '))
if (desejo/anos)/12 <= 0.3*salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')