a=float(input("O valor da casa a comprar "))
b=float(input("Salário "))
c=int(input("Quantidade de anos a pagar "))
if a/c*12 <= b*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')