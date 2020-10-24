casa=float(input("qual o valor da casa a comprar? "))
salario=float(input("qual seu salário? "))
anos=float(input("em quantos anos voce quer pagar? "))

prestaçao=casa/(anos*12)
if prestaçao>salario*0.30:
   print("Empréstimo não aprovado")
else:
   print("Empréstimo aprovado")