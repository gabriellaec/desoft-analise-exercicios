cigarros = int(input('Quantos cigarros você fuma por dia?: '))
tempo = int(input('Há quanto tempo você fuma?: '))
vida = (((cigarros*365)*tempo)*10)/1440 
print('Você já perdeu {0}'.format(vida) + ' dias de vida!')