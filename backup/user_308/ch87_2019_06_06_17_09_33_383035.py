import csv
custo=0   
with open ('churras.txt') as lista:
	consumo=csv.reader(lista)
	for row in consumo:
   		x=row.split(',')
   		custo+=x[1]*x[2]
    
print(custo)          


