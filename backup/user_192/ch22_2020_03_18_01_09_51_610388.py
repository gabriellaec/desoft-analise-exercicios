cigarros = input('Quantos cigarros você fuma por dia? ')
anos = input('Há quantos anos fuma? ')

tempo_perdido = (int(((cigarros*365)*anos)*10)//1440)
    
print('Seu tempo de vida perdido é {} dias').format(tempo_perdido)
