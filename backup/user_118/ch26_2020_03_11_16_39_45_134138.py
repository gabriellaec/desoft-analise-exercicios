def prestacao (a,b,c):
    p=(a/c*12)
    return p
x=int(input('Valor da casa:'))
y=int(input('Salário:'))
z=int(input('Quantidade de anos a pagar:'))
k=prestacao (x,y,z)
if k>((0.3)*y):
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')