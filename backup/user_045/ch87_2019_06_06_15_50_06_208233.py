with open('churras.txt','r') as arquivo:
	conteudo = arquivo.readlines()
	s=0
	for l in conteudo:    	
		l=l.replace('','')
		l=l.split(",")
		s+=l[1]*l[2]
print(s)
       
            
    
    