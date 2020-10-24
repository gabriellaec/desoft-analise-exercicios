def medias_por_inicial(x):
    z = dict()
    
    
    for k,v in x.items():
            z[k[0]] = v
            for m,n in x.items():
                if k[0] == m[0] and k != m:
                    z[k[0]] += (n-v)/2
                
            
    return z

    