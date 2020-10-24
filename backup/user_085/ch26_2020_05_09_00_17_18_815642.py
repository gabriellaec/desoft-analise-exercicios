valor_casa = float(input('Digite o valor da casa a comprar: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Digite por quantos anos você pagará: '))
prestacao_mensal = valor_casa/12
quantidade_de_prestacoes = prestacao_mensal * anos
if (salario * 0.3) < prestacao_mensal:
    print('Empréstimo não aprovado')
else:
  print('Empréstimo aprovado')