with open('churras.txt','r') as arquivo:
	conteudo = arquivo.readlines()
	s=0
	for l in conteudo:    	
		l=l.replace('','')
		l=l.split(",")
		s+=int(l[1])*int(l[2])
print(s)
       
            
    
    