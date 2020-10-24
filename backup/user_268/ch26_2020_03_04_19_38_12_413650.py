v = float(input("valor da casa"))
s = float(input("salário"))
a = float(input("anos para pagar"))
p = v/(a*12)
if p <= s * 0.3:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')