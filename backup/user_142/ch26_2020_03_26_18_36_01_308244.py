casa = float(input('qual o valor da casa?'))
salario = float(input('qual o seu salario?'))
anos = int(input('quantos anos para pagar?'))
meses = 12*anos
prestacao = casa/meses
if prestacao <= salario*0.3:
    print('Empréstimo aprovado')
else:
    print('Emprestimo não aprovado')
 