dias = int (input( "Digite os dias:"))
horas = int (input ("Digite as horas")) 
minutos = int (input("Digite os minutos"))
segundos = int (input ("Digite os segundos"))
d = (dias*24)*3600
h = horas * 3600
m = 60 * minutos
s = segundos
print (d+h+m+s)