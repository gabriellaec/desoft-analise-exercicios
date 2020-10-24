dias = int ( input ('Dias: '))
horas = int( input ('Horas: '))
minutos = int (input ('Minutos: '))
segundos = int ( input ('Segundos: '))

segmin = minutos * 60 
seghoras = horas * 3600 
segdias = dias * 86400

totalseg = segundos + segmin + seghoras + segdias 

print ('\nO total de segundos é igual a', totalseg)