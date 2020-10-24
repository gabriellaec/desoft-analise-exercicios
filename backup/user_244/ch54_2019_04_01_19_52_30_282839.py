def junta_nome_sobrenome(x, y): 
    i = 0 
    z = []*len(x)
    
    
    while i < len(x):
        z.append("{0} {1}".format(x[i], y[i]))
        i += 1
    return z 
x = ["murilo", "enrico", "enzo", "joao"]
y = ["menezes", "costa", "vidigal", "zsigmond"]
print(junta_nome_sobrenome(x,y))
                                
                                
                              
    