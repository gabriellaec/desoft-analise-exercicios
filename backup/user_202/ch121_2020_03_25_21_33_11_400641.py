def subtracao_de_listas(x, y):
    t1 = len(x)
    t2 = len(y)
    i = 0
    lista3 = []
    while i < t1: 
        v = x[i]
        a = 0
        c = False
        f = False
        while a < t2:
    	    if v != y[a]:
                c = False
                f = f+c
                a += 1
           	else:
                c = True
                f = f+c
    		    a += 1
        if f == 0:
            lista3.append(v)
        i += 1
    return(lista3)
        
        