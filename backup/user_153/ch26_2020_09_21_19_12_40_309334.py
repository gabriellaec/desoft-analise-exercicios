valor = int(input("Qual o valor da casa? "))
salario = int(input("Qual o valor do seu salário? "))
anos = int(input("Em quantos anos vai pagar? "))
prestacao = valor/(12*anos)
if 0.3*salario > prestacao:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')