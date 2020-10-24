with open('churras.txt','r') as arquivo:
    quantidade=[]
    preco=[]
    total=0
    i=0
    lines=arquivo.read()
	arroz=lines.split(,)
	quantidade.append(arroz[::2])
    preco.append(arroz[::3])
    while i<len(quantidade):
        total+=quantidade[i]*preco[i]
	print(total)
                          
                          
                 
     
        
	