casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do salário? '))
anos = float(input('Qual a quantidade de anos? '))

prestacao = casa/anos*12

if prestacao > salario*0,30:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')
  