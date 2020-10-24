def prestacao (a,b,c):
    p=(a/c*12)
    return p
x=float(input('Valor da casa:'))
y=float(input('Salário:'))
z=float(input('Quantidade de anos a pagar:'))
k=prestacao (x,y,z)
if k>((0.3)*y):
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')