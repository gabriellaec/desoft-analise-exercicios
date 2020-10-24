def estritamente_crescente (list):
    if len(list) <= 1:
        return list
    
    result = [ list[0] ]
    
    for number in list[1:]:
        if number > result[-1]:
            result.append(number)
            
    return result
