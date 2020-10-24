casa = float(input("qual o valor da casa?"))
salario = float(input("qual o seu salario?"))
anos = float(input("quantos anos vc deve pagar?"))

valor = casa/anos*12

if valor>=salario*0.3:
    print ("Empréstimo não aprovado")
else:
    print ("Empréstimo aprovado")