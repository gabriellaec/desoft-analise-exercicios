C = int(input('quantos cigarros por dia?:'))
A = int(input('quantos anos vc fuma?:'))
AN = 525600*A
D = 1440 
TVP = (10*C*AN)/D
print('voce ja perdeu {0} minutos de vida'.format(TVP))