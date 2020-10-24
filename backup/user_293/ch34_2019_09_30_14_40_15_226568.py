capital = int(input("Qual o depósito inicial? "))
c0 = capital
taxa = int(input("Qual a taxa de juros da poupança? "))
tempo = 0
while tempo < 25:
    juros = capital*taxa
    print('{0:.2f}'.format(juros))
    capital = juros
    tempo += 1
print('{0:.2f}'.format(juros-c0))
    