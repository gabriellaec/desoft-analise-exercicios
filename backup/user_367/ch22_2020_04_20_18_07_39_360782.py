p=int(input('Quantos cigarros: '))
o=int(input('Quantos anos: '))
cigarros= (p*360) * o 
tempo= (cigarros *10)/144
print('dias a menos: {0}' .format(tempo))