x = input('valor da casa')
y = input('salário')
z = input('quantos anos')

casa = float(x)
salario = float(y)
meses = int(z) * 12
prestacao = casa / meses

if prestacao > salario * 0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')