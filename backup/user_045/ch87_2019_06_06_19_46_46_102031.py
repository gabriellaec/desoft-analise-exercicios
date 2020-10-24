with open('churras.txt','r') as arquivo:
	conteudo = arquivo.readlines()
	s=0
	for l in conteudo:    	
		
		l=l.split(",")
		s+=float(l[1])*float(l[2])
print(s)
       
            
    
    