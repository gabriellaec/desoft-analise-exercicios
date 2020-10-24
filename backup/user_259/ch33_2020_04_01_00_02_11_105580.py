def primos_entre(a,b):
    vaal = []
    for val in range(a, b + 1): 
        if val > 1: 
            for n in range(2, val): 
                if (val % n) == 0: 
                    break
                else: 
                    vaal.append(val) 
    return len(vaal)
     
                
