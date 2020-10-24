a = int(input("qual o valor da casa? : "))
b = int(input("qual o seu salário? : "))
c = int(input("em quantos anos irá pagar? : "))
prestacao = a / (c/12)
val_mes = b * float(0.3)
if prestacao < val_mes:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")