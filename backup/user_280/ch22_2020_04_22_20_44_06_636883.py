quantidade = int(input('Quantos cigarros vc fuma por dia? '))
anos = input('Há quantos anos vc fuma? ')

tempo_perdido = quantidade*10/(60*24*30*12*anos)
tempo = tempo_perdido/365


print(tempo)