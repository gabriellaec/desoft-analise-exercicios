v = int(input("Qual o valor da casa?"))
s = int(input("Qual o seu salário?"))
q = int(input("Em quanos anos deseja pagar?"))
p = (v/q*12)

if p<(s*0.3):
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")