valor= input('valor: ')
salario= input ('salario: ')
anos= input ('anos: ')
total= valor/ (anos *12)
if total< 0.3*salario:
    print ('Empréstimo aprovado')
else:
    print ('Empréstimo não aprovado')