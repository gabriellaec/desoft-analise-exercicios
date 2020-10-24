x = int(input('quanto  custa a casa?'))
y = int(input('qual seu salario?'))
z = int(input('quantidade de anos a pagar?'))
meses = z*12
if x/meses > 0.3*y:
    print ('Empréstimo aprovado')
else:
    print ('Empréstimo não aprovado')
       
             