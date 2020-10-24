val = int(input("Digite o valor da casa "))
sal = int(input("Digite o valor do seu salário"))
ano = int(input("Digite o tempo em anos que pretende pagar "))

calculo = (val/ano)

if calculo <= 0.3*sal:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")