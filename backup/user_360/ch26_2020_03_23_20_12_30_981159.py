v = int(input("Qual o valor da casa?"))
s = int(input("Qual o seu salário?"))
q = int(input("Em quanos anos deseja pagar?"))

p = (v/q)
if p<s:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")