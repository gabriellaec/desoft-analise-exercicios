import csv
custo=0   
with open ('churras.txt') as lista:
	consumo=csv.reader(lista)
	for row in consumo:
   		
   		custo+=row[1]*row[2]
    
print(custo)          


