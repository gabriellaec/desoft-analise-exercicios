with open('macacos-me-mordam.txt','r') as arquivo:
	conteudo = arquivo.read()
    l=conteudo.split(", ")
    c=0
    for i in l:
        g=i.lower()
        if g=='banana':
            c+=1
            
    print(c)