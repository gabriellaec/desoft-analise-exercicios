capital = int(input("Qual o depósito inicial? "))
taxa = int(input("Qual a taxa de juros da poupança? "))
tempo = 1
while tempo < 25:
    juros = capital*taxa*tempo
    print('{0:.2f}'.format(juros))
    capital = juros
    tempo += 1
print('{0:.2f}'.format(juros))
    