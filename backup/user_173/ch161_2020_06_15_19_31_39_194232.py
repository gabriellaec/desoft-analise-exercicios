def PiWallis(elementos):
    numerador,denominador = 2,1
    i = 0
    mul = 1
    while i < elementos:
                
        mul*= numerador/denominador
        if i%2 == 0:
            denominador += 2
        else:
            numerador +=2
        i+=1
    return mul