with open('macacos-me-mordam.txt','r') as arquivo:
    l = arquivo.readlines()
	l=l.replace(' ',',')
    l=l.replace(' ','')
	l=conteudo.split(",")
    c=0
    for i in l:
    	for e in i:
            g=e.lower()
            if g =='banana':
                c+=1
print(c)