dias = float(input("Quantos cigarros você fuma por dia? "))
anos = float(input("Há quantos anos você fuma? "))

perda = (dias*144 + anos*52560)/1440
print(perda)