def primos_entre(a, b):
    i = a
    resultado = []
    divisor = 2
    while i <= b and divisor < b:
        if i % divisor != 0:
            divisor += 1
        else:
            i += 1
            
    resultado.append(i)
    
    return resultado
            