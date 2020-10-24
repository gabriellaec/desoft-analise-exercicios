def PiWallis(n):
    produtorio = 1
    numerador = 1
    denominador = 1
    i = n # numerador(n par) // denominador (n ímpar)
    j = n + 1 # denominador(n par) // numerador (n ímpar)
    if n == 1:
        produtorio *= 2
    else:
        # Para n par
        if n % 2 == 0:
            while i > 1:
                # Calcula produto do numerador
                numerador *= i*i
                i -= 2
            while j > 1:
                # No denominador, há um termo maior que n e ímpar quando n é par
                if j > n:
                    denominador *= j
                # Se j já não é mais n+1, os termos são em duplas
                else:
                    denominador *= j*j
                j -= 2
            produtorio *= numerador/denominador
        # Para n ímpar
        else:
            while j > 1:
                # Calcula produto do numerador
                if j > n:
                    numerador *= j
                else:
                    numerador *= j*j
                j -= 2
            while i > 1:
                denominador *= i*i
                i -= 2
            produtorio *= numerador/denominador
    return 2*produtorio