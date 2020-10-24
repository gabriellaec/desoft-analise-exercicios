l_p=[]

p=input('Palavra? ')

while p!= 'fim':
	l_p.append(p)
	p=input('Outra palavra ')
    
i=0
while i<len(l_p):
	palavra=l_p[i]
	if len(p) > 1 and p[0]=='a':
    	print(palavra)
   	
i+=1