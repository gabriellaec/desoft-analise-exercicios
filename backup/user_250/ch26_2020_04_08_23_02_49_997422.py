c = float(input("Valor da casa? ")
s = float(input("Salário? ")
t = float(input("Quantos anos? ")
          
m = t*12
p = c/m
q = s*0.3

if p > q:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")