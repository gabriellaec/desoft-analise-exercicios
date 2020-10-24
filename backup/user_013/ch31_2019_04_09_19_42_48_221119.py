#Preço da casa p
p = float(input())
#Salário s
s = float(input())
#Anos a pagar a
a = int(input())
#Valor da mensalidade m 
m = (p / (a*12))
if m > 0.3 *s:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
