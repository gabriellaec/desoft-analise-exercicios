a=int(input('qual é o valor da casa? '))
b=int(input('qual é o seu salario? '))
c=int(input('quantidade de anos a pagar? '))
if a/c*12<=b*0.3:
    print ('Empréstimo aprovado')
else:
    print ('Empréstimo não aprovado')