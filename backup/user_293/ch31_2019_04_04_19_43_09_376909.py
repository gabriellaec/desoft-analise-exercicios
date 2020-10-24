valor_casa = int(input("Quanto custa o valor da casa?: "))
salario = int(input("Qual é o seu salário?: "))
anos = int(input("Em quantos anos vai pagar?: "))
prestacao = valor_casa/(anos*12)
if prestacao < salario*(30/100):
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')
