cig = int(input("Digite o número de cigarros "))
ano = int(input("Digite o número de anos "))


calculo = (ano * 365 * 0,694445 * 10**(-3) * (10*cig))

print('O número de dias perdidos foi de {0}'.format(calculo))
             