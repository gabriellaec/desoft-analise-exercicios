def piWallis(numero):
    contador = 0
    numerador = 2
    denominador = 1

    while contador <= numero:

        if numerador < denominador:
            numerador *= 2
        
        if denominador < numerador:
            denominador *= 2

    return (numerador/denominador)*2

print(piWallis(5))        
