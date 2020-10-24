valor_casa = int(input('Valor da casa: '))
salario = int(input('Valor do salário: '))
anos = int(input('Quantidade de anos: '))
meses = anos * 12
prestacao = valor_casa/meses
if prestacao <= 0.3 * salario:
  print('Empréstimo aprovado')
elif prestacao > 0.3 * salario:
  print('Empréstimo não aprovado')