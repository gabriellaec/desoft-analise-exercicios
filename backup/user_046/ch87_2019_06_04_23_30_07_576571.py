with open('churras.txt','r') as arquivo:
    quantidade=[]
    preco=[]
    total=0
    i=0
    z=1
    y=2
    lines=arquivo.read()
	arroz=lines.split(',')
      
    quantidade.append(float((arroz[z]))
    preco.append(float(arroz[y]))
    z+=2
    y+=2
    while i<len(quantidade):
        total+=quantidade[i]*preco[i]
        
	