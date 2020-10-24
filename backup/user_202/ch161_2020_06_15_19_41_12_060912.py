def PiWallis(n):
    i = 1
    numerador = 0
    denominador = 0
    conta = 0
    resultado = 0
    while i <= n:
        if i%2 == 0:
            numerador = i
            denominador = i+1
            conta = numerador/denominador
        else:
            numerador = i+1
            denominador = i
            conta = numerador/denominador
        resultado *= conta    
        i += 1
    return resultado*2
        
    