def encontra_maximo(lista):
    norm_inf = 0
    for e in lista:
        for a in e:
            if abs(a) > norm_inf:
                norm_inf = abs(a)
    return norm_inf    
    
    
    
    
    
    
  