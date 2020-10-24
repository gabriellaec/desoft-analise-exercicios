def juntar_nome_sobrenome(x, y): 
    i = 0 
    z = []*len(x)
    
    
    while i < len(x):
        z.append("{0} {1}".format(x[i], y[i]))
        i += 1
    return z 

x = ["murilo", "enrico"]
y = ["menezes", "costa"]                            
print(juntar_nome_sobrenome(x,y))
                                
                                
                              
    