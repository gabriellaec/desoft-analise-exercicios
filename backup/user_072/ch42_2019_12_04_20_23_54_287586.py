#def quantos_uns(n):
#    i=0
#    soma_de_uns=0
#    lista= str(n).split(',')
#    while i<len(lista):
#        if i==1:
#            soma_de_uns+=1
#    return soma_de_uns
#print (quantos_uns)
        
def quantos_uns(x):
	uns = [] 
	x = str(x)
	for i in x:
        
		if i == '1':
			uns.append(i)
	return len(uns)