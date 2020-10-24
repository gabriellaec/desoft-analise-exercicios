dinicial = int(input("Qual o deposito inicial?"))
dmensal = int(input("Qual o deposito mensal?"))
txjuros = int(input("Qual a taxa de juros?"))
valor = dinicial

i = 0
while i <= 23:
    valor += dmensal*(txjuros)**(i-1)
    i+=1
    print("Ganho foi de {0:.2f}".format(valor))
print("Ganho foi de {0:.2f}".format(valor))