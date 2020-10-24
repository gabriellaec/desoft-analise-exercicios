x = int(input('valor da casa: '))
y = int(input('salário: '))
z = int(input('quantidade de anos: '))
if x/(12*z)>0.3*y:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')