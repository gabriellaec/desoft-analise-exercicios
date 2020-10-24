a=float(input("Qual é o valor da casa?: "))
b=float(input("Qual é o seu salário?: "))
c=int(input("Em quantos meses você vai pagar a casa?: "))
prestacao_mensal=a/c
if prestacao_mensal>0.3*b:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')