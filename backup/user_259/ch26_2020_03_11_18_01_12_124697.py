valor=int(input("Qual o valor da casa? "))
salario=int(input("Qual é o seu salário? "))
tempo=int(input("Em quanto tempo? "))
meses=tempo*12
prestação=valor/meses
if prestação>(salario*1.3):
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
      