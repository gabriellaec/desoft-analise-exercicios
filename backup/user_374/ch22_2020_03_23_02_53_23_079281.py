um = input("Digite o número de cigarros ")
cig = int(um)
dois = input("Digite o número de anos ")
ano = int(dois)

calculo = ((cig*10) * 0,694444 * (10**(-2)) * (ano*365))

print('O número de dias perdidos foi de {0}'.format(calculo))