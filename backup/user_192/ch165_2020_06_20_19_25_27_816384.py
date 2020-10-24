def mais_populoso(x):
    z = []
    for muni, dic2 in x.items():
        for estado, hab in x[muni].items():
            z.append(x[muni][estado])
    maior = max(z)
    if x[muni][estado] == maior:
        return estado
            
            
            
            
            
            