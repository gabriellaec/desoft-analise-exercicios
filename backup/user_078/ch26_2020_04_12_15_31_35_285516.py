casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do salário? '))
anos = float(input('Qual a quantidade de anos? '))
meses = anos*12
prestacao = casa/meses

if prestacao/12 > salario*0.30:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')
  