def piWallis(numero):
    contador = 0
    numerador = 2
    denominador = 1

    conta = 2

    while contador <= numero:

        if numerador <= denominador:
            numerador += 2
            conta *= numerador/denominador


        elif denominador <= numerador:
            denominador += 2
            conta *= numerador/denominador

        contador += 1
    
    return conta*2
