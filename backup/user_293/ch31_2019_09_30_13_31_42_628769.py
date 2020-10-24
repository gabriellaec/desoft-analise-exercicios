valor = int(input("Qual o valor da casa a comprar? "))
salario = int(input("Qual o seu salário? "))
tempo = int(input("Quantidade de anos a pagar? "))

prestacao = valor/(tempo*12)

if prestacao <= 0.3*salario:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')