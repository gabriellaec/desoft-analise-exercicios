c = input('valor da casa')
s = input('salário')
m = input('anos a pagar')*12
p= c/m
if p > 0.3*s:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado´)