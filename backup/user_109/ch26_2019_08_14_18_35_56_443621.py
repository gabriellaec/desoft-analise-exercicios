def n(a, c):
    tempo = ((a*365)*c)*10
    return tempo

a = int(input('Insira há quantos anos você fuma: '))
c = int(input('Insira quantos cigarros você usa por dia: '))

print(n(a, c))