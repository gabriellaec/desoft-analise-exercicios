a= int(input("Qual o valor da casa a comprar?"))
b= int(input("Qual o salário?"))
c= int(input("Qual a quantidade de anos a pagar?"))

prestacão = a/12*c 

if prestacão < 0.3*b:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")