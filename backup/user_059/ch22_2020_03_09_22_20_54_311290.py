dia = int(input('Quantos cigarros você fuma por dia? '))
ano = int(input('Há quantos anos você fuma? '))

totalcigarro = (dia*(ano*365))
vidaperdida = (totalcigarro*10)/1440

print(vidaperdida)