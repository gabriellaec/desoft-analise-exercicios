a=float(input("Qual o valor da casa?"))
b=input("Salario:")
c=int(input("Anos a pagar"))
d=a/(c*12)
if d>(0.3*b):
    return "Empréstimo não aprovado"
else:
    return "Empréstimo aprovado"