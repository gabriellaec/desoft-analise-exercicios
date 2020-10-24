def mais_populoso(x):
    z = []
    for k, v in x.items():
        for estado, hab in x[k].items():
            return x[k][estado] == max(hab)
            
            
            
            