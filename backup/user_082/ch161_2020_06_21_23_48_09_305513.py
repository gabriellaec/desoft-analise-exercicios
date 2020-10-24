def PiWallis(n):
    numerador = 2
    denominador = 1
    sum = 1

    if n == 1:
        return 4
    else:
        for i in range(0,n):
            sum *= numerador / denominador
            
            if i % 2 == 0:
                denominador += 2
            else:
                numerador += 2
            return sum * 2