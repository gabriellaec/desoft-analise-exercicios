a=int(input("O valor da casa a comprar "))
b=int(input("Salário "))
c=int(input("Quantidade de anos a pagar "))
d=c*12
prestacao=a/d
if prestacao > b*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')