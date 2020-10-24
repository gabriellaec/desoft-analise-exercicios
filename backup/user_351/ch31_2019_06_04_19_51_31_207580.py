casa=float(input("qual o valor da casa a comprar? "))
salario=float(input("qual seu salário? "))
anos=float(input("em quantos anos voce quer pagar? "))
valor=salario*0.30
prestaçao=valor/(anos*12)
if prestaçao>=valor:
   print("Empréstimo não aprovado")
else:
   print("Empréstimo aprovado")