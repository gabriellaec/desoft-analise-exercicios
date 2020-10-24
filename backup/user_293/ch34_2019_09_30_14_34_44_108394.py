capital = int(input("Qual o depósito inicial? "))
taxa = int(input("Qual a taxa de juros da poupança? "))
tempo = 1
while tempo < 25:
    juros = capital*taxa*tempo
    print(juros:.2f)
    capital = juros
    tempo += 1
print(juros:.2f)
    