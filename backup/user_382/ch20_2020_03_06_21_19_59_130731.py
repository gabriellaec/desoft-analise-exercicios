qnto_km = float(input('Qual a distancia que deseja percorrer?'))
	
if  0<= qnto_km < 200:
	total = qnto_km*0.5 
else:
	total = 200*0.50 + (qnto_km-200)*0.45

total_d = round(total,2)
        
print (total_d)