def PiWallis(n):
    numerador = 2
    denominador = 1
    soma = 1

    if n == 1:
        return 4
    else:
        for i in range(0,n):
            soma *= numerador / denominador
            
            if i % 2 == 0:
                denominador += 2
            else:
                numerador += 2
            return soma * 2