with open('churras.txt','r') as arquivo:
    quantidade=[]
    preco=[]
    total=0
    i=0
    lines=arquivo.read()
	colunas = lines.split(';')
	quantidade.append(arroz[1::2])
    preco.append(arroz[2::2])
    while i<len(quantidade):
        total+=quantidade[i]*preco[i]
	print(total)
                          
                          
                 
     
        
	