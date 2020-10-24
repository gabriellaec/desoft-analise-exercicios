valor= int(input('valor: '))
salario= int(input ('salario: '))
anos= int(input ('anos: '))
total= valor/ (anos *12)
if total< 0.3*salario:
    print ('Empréstimo aprovado')
else:
    print ('Empréstimo não aprovado')