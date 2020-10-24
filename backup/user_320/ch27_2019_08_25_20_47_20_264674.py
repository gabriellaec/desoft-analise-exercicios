pigas = int(input('Quantos cigarros você fuma por dia: '))
anos = int(input('A quantos anos você fuma: ')) * 365
roubo = pigas * anos 
dia = 24 * 60
roubo = roubo * (10/dia)
print(int(roubo))