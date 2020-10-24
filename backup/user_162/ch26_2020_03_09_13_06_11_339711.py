vc = float(input("Qual o valor da casa? "))
s = float(input("Quanto você ganha? "))
m = float(input("Em quantos anos vai pagar? "))*12
PM = float(vc/m)

if PM > 0.3*s:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")