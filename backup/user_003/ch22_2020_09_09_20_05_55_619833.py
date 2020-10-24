cigarro = int(input("Quantos cigarros voce fuma por dia?  "))
anos = int(input("Há quantos anos fuma?  "))

cigarrosvida = (365 * anos) * cigarro

minsvida = cigarrosvida * 10

hrsvida = minsvida / 60

diasvida = hrsvida / 24

print(diasvida)