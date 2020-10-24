valor=float(input("Qual o valor da casa: ")
salario=float(input("Qual o seu sálario: ")
anos=int(input("Quantos anos a pagar: ")
if ((valor/(anos*12))<=salario*0.3):
    print ("Empréstimo aprovado")
else:
    print ("Empréstimo não aprovado")