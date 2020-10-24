valor_da_casa = float(input("Qual o valor da casa?"))
salario = float(input("Qual o seu salário?"))
n = float(input("Qual a quantidade de anos a pagar?"))

prestacao = valor_da_casa / (n * 12)

if prestacao > (salario * 0.3):
    print("Empréstimo não aprovado")
elif prestacao <= salario * 0.3:
    print("Empréstimo aprovado")