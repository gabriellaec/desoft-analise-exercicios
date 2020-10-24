valor_casa = float(input('Qual o valor da casa?'))
salario = float(input('Quanto é o salário?'))
qnt_anos = float(input('Quantidades de anos a pagar'))

if valor_casa/(qnt_anos*12) > 0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
    