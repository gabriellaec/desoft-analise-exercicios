a=input('Valor da casa: ')
b=input('Valor do salário: ')
c=input('Quantidade de anos: ')
p=a/c*12
if p>0.3*b:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')