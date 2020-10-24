a=input('Valor da casa: ')
b=input('Valor do salário: ')
c=input('Quantidade de anos: ')
if p>0.3*b:
    p=a/c*12
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')