def prestacao (a,c):
    p=(a/c)*12
    return p
x=int(input('Valor da casa:'))
y=int(input('Salário:'))
z=int(input('Quantidade de anos a pagar:'))
k=prestacao (x,z)
if k>(3/10)*y:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')