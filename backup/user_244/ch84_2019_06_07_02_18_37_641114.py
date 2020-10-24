def inverte_dicionario(x):
    y = dict()
    
    for k,v in x.items():
        if v not in y:
            y[v] = []
        y.append(k)
        
    return y



        
        

        