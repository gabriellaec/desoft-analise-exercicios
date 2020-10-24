def calcula_fibonacci(n):
    result = []
    
    if n < 1:
        return result
    
    result.append(1)
    
    if n == 1:
        return result
    
    result.append(1)
    
    if n == 2:
        return result
    
    i = 2
    
    while i < n:
        result.append(result[i-1] + result[i-2])
        i = i + 1
        
    return result