def prestacao (a,c):
    p=(a/c*12)
    return p
x=int(input('Valor da casa:'))
y=int(input('Salário:'))
z=int(input('Quantidade de anos a pagar:'))
k=prestacao (x,z)
if k>((0.3)*y):
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')