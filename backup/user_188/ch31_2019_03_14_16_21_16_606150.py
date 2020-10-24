valor_casa = float(input("Qual é o valor da casa? "))
salario = float(input("Quanto é o salário? "))
anos = int(input("Em quantos anos seria paga? "))

prestacao = valor_casa / (anos * 12)

if prestacao > (salario * 0.3):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')