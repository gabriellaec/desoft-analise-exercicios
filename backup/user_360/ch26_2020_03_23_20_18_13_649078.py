valor = int(input("Qual o valor da casa?"))
salario = int(input("Qual o seu salário?"))
tempo = int(input("Em quantos anos deseja pagar?"))

prestacao = (valor/(tempo*12))

if prestacao<=(salario*0.30):
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")