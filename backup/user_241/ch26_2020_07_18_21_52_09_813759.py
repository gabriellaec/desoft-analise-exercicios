x = int(input("Qual o valor da casa ? "))
y = int(input("Qual o salário ? "))
z = int(input("Quantidade de anos a pagar ? "))
a = x/(z * 12)
if a > 0.3 * y:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')