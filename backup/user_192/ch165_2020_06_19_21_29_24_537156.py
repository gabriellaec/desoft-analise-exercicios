def mais_populoso(x):
    z = []
    for k, v in x.items():
        for estado, hab in v.items():
            maior = max(hab)
            return v[estado] == maior
            
            
            
            
            