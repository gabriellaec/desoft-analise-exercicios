def encontra_maximo(m):
    max = ''
    for i in m:
        for a in i:
            if abs(a) > abs(max):
                max = a 
                
            
        