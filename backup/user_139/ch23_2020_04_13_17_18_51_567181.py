resp = int(input ('Qual a velocidade (km/h)? '))
if resp > 80:
    x = 5 * (resp - 80)
    print ('A multa é: R${0:.2f}'.format(x)
else:
    print ('Não foi multado')