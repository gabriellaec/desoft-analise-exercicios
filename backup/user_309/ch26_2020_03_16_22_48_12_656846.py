valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salario: '))
anos = int(input('Digite em qts anos pretnde pagar: '))

prestacao = valor_casa/(anos*12)
if prestacao > (salario*0.30):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
    
