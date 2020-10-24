a=float(input("Qual é o valor da casa?: "))
b=float(input("Qual é o seu salário?: "))
c=int(input("Em quantos meses você vai pagar a casa?: "))
prestacao_mensal=a/c
if prestacao_mensal<=(1/3)*b:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')