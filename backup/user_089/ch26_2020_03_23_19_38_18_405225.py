a= float(input(" Qual o valor da casa a comprar?"))
b= float(input(" Qual o salário?"))
c= float(input(" QUal a quantidade de anos a pagar?"))

prestação = a/12*c 

if prestação < 0.3*b:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")