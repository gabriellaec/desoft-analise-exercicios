preco=float(input('valor da casa'))
sal=float(input('salario'))
t=int(input('anos a pagar'))
prest=preco/(t*12)
if prest>0.3*sal:
    print ('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')