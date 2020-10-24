c = float(input('valor da casa'))
s = float(input('salário'))
a = float(input('anos a pagar'))
p= c/(12*a)
if p > 0.3*s:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado´)