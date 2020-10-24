import csv

with open("churras.txt", "r") as banana:
    conteudo = csv.reader (banana)
    
	i=0
    
	for row in conteudo:
    	i+= row[1]*row[2]
	print (i)
        