forma = float(input('Qual a sua velocidade? \n'))
if forma > 80:
    m = 5 * (forma - 80)
    print('Você foi multado em: ',m)
    

else:
    print('Você não levou multa.')