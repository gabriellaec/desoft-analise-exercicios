capital = float(input("Qual o depósito inicial? "))
taxa = float(input("Qual a taxa de juros da poupança? "))
tempo = 1
while tempo < 25:
    juros = capital*((1 + taxa)**tempo)
    print('{0:.2f}'.format(juros))
    tempo += 1
print('{0:.2f}'.format(juros))
    