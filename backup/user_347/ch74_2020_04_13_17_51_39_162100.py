def conta_bigramas(texto):
        dic = {}
        a = 0
        
        for i in len(texto)-1:
            bigrama = texto[a] + texto[a+1]
            a += 1
            
            if bigrama not in dic:
                dic[bigrama] = 1
            else:
                dic[bigrama] += 1
        return dic