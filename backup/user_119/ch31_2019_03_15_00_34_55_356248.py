valor=int(input('Valor da casa: '))
sal=int(input('Seu salario: '))
ano=int(input('Quantos anos: '))
y=valor/(12*ano)
if y>0.3*sal:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')
          