def PiWallis(numero):
    numerador = 2 
    denominador = 1
    conta = 1
    for num in range(numero):
        if num%2 !=0:
            conta *= numerador/denominador
            denominador+=2
        else:
            conta*= numerador/(denominador+2)
            numerador += 2
    return conta