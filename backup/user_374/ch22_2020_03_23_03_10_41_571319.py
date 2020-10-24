cig = int(input("Digite o número de cigarros "))
ano = int(input("Digite o número de anos "))

minutos = 10 * cig
dias = 365 * ano

calculo = (minutos * (1/1440) * dias)

print('O número de dias perdidos foi de {0}'.format(calculo))
              
              