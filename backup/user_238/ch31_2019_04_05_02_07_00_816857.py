valor=float(input('valor '))
salario=float(input('salario '))
anos=float(input('anos '))

prestacao=valor/(anos*12)
if prestacao > 0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
