def mais_populoso(x):
    s = 0
    pop = ''
    for muni in x.keys():
        for estado, hab in x[muni].items():
            d = sum(x[muni].values())
        if d > s:
            s = d
            pop = muni
    return pop

            
            
            
            
            