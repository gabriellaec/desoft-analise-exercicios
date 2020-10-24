v = int(input('valor'))
s = int(input('salario'))
q = int(input('anos'))
p = v/(q*12)
if p >= s*0.3 :
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')