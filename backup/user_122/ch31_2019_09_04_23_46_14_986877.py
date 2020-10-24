valor_da_casa = float(input("Qual o valor da casa?"))
salario = float(input("Qual o seu salário?"))
n = int(input("Qual a quantidade de meses a pagar?"))

prestacao = valor_da_casa / n

if prestacao > (salario * 0.3):
    print("Empréstimo não aprovado")
elif prestacao <= (salario * 0.3):
    print("Empréstimo aprovado")