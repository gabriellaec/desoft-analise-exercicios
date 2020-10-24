casa= float(input('Qual o valor da casa? '))
salario= float(input('Quanto é seu salário? '))
anos= float(input('Quantidade de anos a pagar? '))
if casa/(anos*12) >0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')