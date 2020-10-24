import csv

with open ('churras.txt') as lista:
	consumo=csv.reader(lista)
custo=0   
for row in consumo:
    x=row.split(',')
    custo+=x[1]*x[2]
    
print(custo)          


