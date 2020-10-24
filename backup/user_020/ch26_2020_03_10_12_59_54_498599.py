preco = int(input("Qual o preço total da casa?"))
salario = int(input("Qual o seu salário?"))
tempo = int(input("Em quantos anos você deseja pagar a casa?"))
prestacao = preco/tempo
if prestacao > (0.3)*(salario):
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")