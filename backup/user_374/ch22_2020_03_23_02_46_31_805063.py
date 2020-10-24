um = input("Digite o número de cigarros ")
cig = int(um)
dois = input("Digite o número de anos ")
ano = int(dois)

calculo = ((cig*10)*0,694444* 10**(-3) + (ano*365))

print(calculo)