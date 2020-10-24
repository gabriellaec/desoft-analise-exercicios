c = float(input("Qual o valor da casa que deseja comprar? "))
s = float(input("Qual é o seu salário? "))
t = float(input("Em quantos anos pretende quitar a casa? "))

def valor_parcela(c,s,t):
    y = c/(t*12)
    if y > 0.3*s:
        return "Empréstimo não aprovado"
    else:
        return "Empréstimo aprovado"

print(valor_parcela(c,s,t))
