valor=float(input("Qual o valor da casa a comprar? "))
sal=float(input("Qual seu salário? "))
t=int(input("Em quantos anos deseja pagar? "))
presta=valor/(t*12)
if presta<=0.3*sal:
    print("Empréstimo aprovado")
else: print("Empréstimo não aprovado")
    