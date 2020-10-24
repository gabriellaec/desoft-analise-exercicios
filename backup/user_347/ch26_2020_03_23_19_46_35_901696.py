a = float(input("Qual o valor da casa a comprar?"))
b = float(input("Qual seu salário?"))
c= int(input("Qual a quantidade de anos a pagar?"))
                
prestação = a/(12*c)

if prestação <0.3*b:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")