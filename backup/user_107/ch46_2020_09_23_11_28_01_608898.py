def numero_no_indice (list):
    result = []
    
    for i in range(0, len(list)):
        item = list[i]
        
        if i == item:
            result.append(item)
            
    return result
