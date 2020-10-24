from collections import Counter 

def bairro_mais_custoso(dg):
    ds = {}
    soma = 0

    for k, v in dg.items():
        v2 = v[6:12]
        for i in v2:
            soma += i            
            
        ds[k] = soma   
    
    k = Counter(ds) 
    m = k.most_common(1)    
    
    
    return m