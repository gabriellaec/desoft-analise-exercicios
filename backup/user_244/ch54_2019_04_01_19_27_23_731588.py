def juntar_nome_sobrenome(x, y): 
    i = 0 
    z = []
    
    while i < len(x):
        z[i] = "{0} {1}".format(x[i], y[i])
	return z 

x = ["murilo", "enrico"]
y = ["menezes", "costa"]                               
print(juntar_nome_sobrenome(x,y))
                                
                                
                              
    