valor_casa=float(input("preco:"))
salario=float(input("salario:"))
anos=float(input("anos:"))
if valor_casa/anos > 0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
