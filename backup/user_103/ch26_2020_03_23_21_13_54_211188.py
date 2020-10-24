a=float(input("Qual é o valor da casa?: "))
b=float(input("Qual é o seu salário?: "))
c=int(input("Em quantos anos você vai pagar a casa?: "))
prestacao_mensal=(a/(c*12))
if prestacao_mensal<=(0.3)*b:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')