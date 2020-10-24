vcc = float(input("Insira o valor da casa a comprar: "))
sal = float(input("Insira o seu salário: "))
tempo = int(input("Insira o número de anos que deseja pagar: "))
vpm = vcc/(tempo*12)
print (vpm)
if vpm<(0.3*sal):
    print ("Empréstimo aprovado")
else:
    print ("Empréstimo não aprovado")
    