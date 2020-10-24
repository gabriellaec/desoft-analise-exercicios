def eh_crescente (list):
    if len(list) < 1:
        return False
    
    result = [ list[0] ]
    
    for number in list[1:]:
        if number > result[-1]:
            result.append(number)
            
    return len(list) > 0