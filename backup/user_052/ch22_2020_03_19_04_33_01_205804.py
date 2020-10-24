cigarros = int(input("Quantos cigarros você fuma por dia?"))
anos = int(input("Há quantos anos você fuma?"))
total = 100 - ((cigarros*365+anos)*0.006944)
print (total)