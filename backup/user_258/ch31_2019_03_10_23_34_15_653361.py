a=int(input('Valor da casa: '))
b=int(input('Valor do salário: '))
c=int(input('Quantidade de anos: '))
p=a/c*12
if p>0.3*b:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')