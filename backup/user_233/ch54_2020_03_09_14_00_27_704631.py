def calcula_fibonacci(inteiro):
    
    if inteiro == 0: return []
    if inteiro == 1: return [1]
    
    resultado = [1, 1]
    
    index = 2
    
    while len(resultado) < inteiro:
        
        resultado.append(resultado[index - 1] + resultado[index - 2])
        index += 1
        
    return resultado