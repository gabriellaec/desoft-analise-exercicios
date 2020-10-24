a=int(input("Qual o valor da casa?"))
b=int(input("Salario:"))
c=int(input("Anos a pagar"))
d=a/(c*12)
if d>(0.3*b):
    print ("Empréstimo não aprovado")
else:
    print ("Empréstimo aprovado")