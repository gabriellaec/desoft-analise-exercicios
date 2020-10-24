deposito = float(input("Qual é o depósito inicial? "))
taxa = float(input("Qual é a taxa de juros? "))

contador = 1
montante = 0
while contador < = 24:
    montante = deposito * (1 + taxa) ** contador
    print(montante)
print(montante - deposito)