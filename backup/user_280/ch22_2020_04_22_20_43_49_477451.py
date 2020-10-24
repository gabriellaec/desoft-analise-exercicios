quantidade = int(input('Quantos cigarros vc fuma por dia? '))
anos = int(input('Há quantos anos vc fuma? '))

tempo_perdido = quantidade*10/(60*24*30*12*anos)
tempo = tempo_perdido/365

if quantidade == 0:
    tempo = 0
if anos == 0:
    tempo = 10


print(tempo)