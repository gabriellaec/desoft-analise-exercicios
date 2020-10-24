with open('churras.txt','r') as arquivo:
    churras = arquivo.readlines()
    total = 0
	for k in churras:
        
        k=k.split(',')
    	total += int(k[1]) * float(k[2])
print(total)