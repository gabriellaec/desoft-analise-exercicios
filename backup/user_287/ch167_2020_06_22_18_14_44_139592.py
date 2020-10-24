def bairro_mais_custoso(gastos):
    dic1 = {}
    dic2 = {}
    
    for k, v in gastos.items():
        dic1[k] = v[6:12]
        
    for i, j in dic1.items():
        dic2[i] = sum(j)
        
    for a, b in dic2.items():
        if b == max(dic2.values()):
            
            return a