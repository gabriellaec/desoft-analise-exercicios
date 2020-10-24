def mais_populoso(dic):
    max_value = 0 
    state = ''
    
    for i in dic:
        value = 0 
        for v in dic[i].values():
            value += v
        if value > max_value:
            max_value = value 
            state = i 
            
    return state 
            
            


            