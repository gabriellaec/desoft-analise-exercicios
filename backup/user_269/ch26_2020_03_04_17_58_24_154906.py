a=int(input("O valor da casa a comprar "))
b=int(input("Salário"))
c=int(input("Quantidade de anos a pagar"))
if a/c*12 <= b*0.3:
    print('Empréstimo não aprovado')
elif a/c*12 > b*0.3:
    print('Empréstimo aprovado')