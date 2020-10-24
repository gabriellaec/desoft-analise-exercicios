vc = int(input("Qual o valor da casa? ")) 
s = int(input("Qual o seu salário? "))
a = int(input("Quantos anos a pagar? "))

p = (vc / a) / 12

if p <= s * 0.3:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")