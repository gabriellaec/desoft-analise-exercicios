v = int(input('velocidade'))
if v <= 80 :
    print('Não foi multado')
else:
    m = (v - 80)*5
    print("Voce Foi Multado! O valor da multa eh {0} ".format(round(m,2))