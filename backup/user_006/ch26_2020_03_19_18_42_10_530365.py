valorcasa=input("Qual o valor da casa?")
salario= input("Qual o salario?")
anos= input("Quantos anos?")

prestacao=valorcasa/(anos*12)

if prestacao>0.3*salario:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")