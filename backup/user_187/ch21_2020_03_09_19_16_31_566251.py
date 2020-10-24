D = int(input('Entre com o número de dias: '))
H = int(input('Entre com o número de horas: '))
M = int(input('Entre com o número de minutos: '))
S = int(input('Entre com o número de segundos: '))
T = D*86400 + H*3600 + M*60 + S 
print(T) 