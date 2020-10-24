c = int(input('valor da casa'))
s = int(input('salário'))
m = (int(input('anos a pagar')))*12
p= c/m
if p > 1.3*s:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado´)