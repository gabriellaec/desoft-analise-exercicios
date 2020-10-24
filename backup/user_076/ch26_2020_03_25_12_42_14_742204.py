a = int(input ("Qual o valor da casa a comprar?"))
b = int(input("Qual o seu salário?"))
c = int(input("Em quantos anos você poderá pagar?"))

def prestação(valor, salário, tempo):
    p = valor / (tempo * 12) 
    return p

if prestação (a,b,c) > 0.3 * b:
    print ("Empréstimo não aprovado")

else:
    print ("Empréstimo aprovado")