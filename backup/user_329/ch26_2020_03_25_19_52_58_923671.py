valor = float(input("Qual o valor da casa?"))
salario = float(input("Qual o seu salário?"))
meses = int(input("Qual a quantidade de meses a pagar?"))

x = valor/meses

if x < salario*0.3:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")