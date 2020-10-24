a = float(input('valor da casa a comprar: '))
b = float(input('seu salario'))
c = int(input('anos a pagar'))
d = c*12
prestacao = a/d
if prestacao<=0.3*b:
    print(Empréstimo aprovado)
else:
    print(Empréstimo não aprovado)