capital = float(input("Qual o depósito inicial? "))
c0 = capital
taxa = float(input("Qual a taxa de juros da poupança? "))
tempo = 1
while tempo < 25:
    juros = capital*(1 + taxa)
    print('{0:.2f}'.format(juros))
    capital = juros
    tempo += 1
print('{0:.2f}'.format(juros))
    