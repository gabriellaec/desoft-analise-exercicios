valor = float(input("Valor da casa: "))
salario = float(input("Valor do salario: "))
ano = float(input("Quantos anos?"))

meses = ano*12

V_prestacao = valor/meses
a = salario*0.3
if V_prestacao<a:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')