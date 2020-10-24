a=input("O valor da casa a comprar ")
b=input("Salário")
c=input("Quantidade de anos a pagar")
if a/c <= b*0.3:
    print('Empréstimo não aprovado')
elif a/c > b*0.3:
    print('Empréstimo aprovado')