valor = int(input())
salario = int(input())
anos = int(input())
prest = valor/(12*anos)
if prest <= 0.3*sal:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')