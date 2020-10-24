casa = float(input("Qual o valor da casa a comprar: "))
salario = float(input("Qual o seu salário: "))
meses = float(input("Em quantos meses você quer pagar: "))
prestação = casa/meses
if (prestação > 0.3*salario):
    print ("Empréstimo não aprovado")
else:
    print ("Empréstimo aprovado")