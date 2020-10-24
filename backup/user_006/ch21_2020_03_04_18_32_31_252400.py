dias =int(input("Digite um numero de dias"))
horas = int(input("Digite um numero de horas"))
minutos = int(input("Digite um numero de minutos"))
segundos= int(input("Digite um numero de segundos"))

totalsegundos= (((dias*24)*60)*60) + ((horas*60)*60) +(minutos*60) + segundos
print(totalsegundos)