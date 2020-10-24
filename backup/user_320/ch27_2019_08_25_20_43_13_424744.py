pigas = int(input('Quantos cigarros você fuma por dia: '))
anos = int(input('A quantos anos você fuma: ')) * 365
roubo = pigas * anos * (10/(24*60)) 

print(int(roubo))