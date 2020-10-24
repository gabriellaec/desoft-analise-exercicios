qnto_km = float(input('Qual a distancia que deseja percorrer?'))
	
if  qnto_km < 200:
	total = format(qnto_km*0.5,'.2f')
else:
	total = format(200*0.50 + (qnto_km-200)*0.45 ,'.2f')
        
print (total)
