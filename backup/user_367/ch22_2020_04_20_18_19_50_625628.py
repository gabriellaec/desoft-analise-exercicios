p=int(input('Quantos cigarros: '))
o=int(input('Quantos anos: '))
cigarros= (p*365) * o 
tempo= (cigarros *10)/1440
print('dias a menos: {0}' .format(tempo))