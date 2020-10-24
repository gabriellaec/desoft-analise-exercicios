x=int(input('casa?: '))
y=int(input('salario?: '))
z=int(input('anos?: '))
conta = x/z*12
if conta > (y*0.3):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
