casa = float(input('Valor da casa: '))
salario = float(input('Qual seu salario? '))
anos = int(input('Em quantos anos pretende pagar? '))

meses = anos*12
prestacao = casa/meses

if prestacao > salario*0.3:
    print ('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')