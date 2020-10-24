cigarros = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Há quantos anos você fuma? '))
result = ((cigarros*10)*365)*anos
perdido = result/1440
print(perdido)