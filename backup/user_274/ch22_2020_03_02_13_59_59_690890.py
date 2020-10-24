dias = float(input("Quantos cigarros você fuma por dia? "))
anos = float(input("Há quantos anos você fuma? "))

perda = (dias*1440 + anos*525600)/1440
print(perda)