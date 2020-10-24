def PiWallis(n_elementos):

    numerador = 0
    denominador = 1
    multiplicacao = 1
    lista_teste = []

    for i in range(1, n_elementos + 1):
        
        if i % 2 == 0:
            denominador += 2
            multiplicacao *= numerador/denominador
            lista_teste.append(multiplicacao)

        else:
            numerador += 2
            multiplicacao *= numerador/denominador
            lista_teste.append(multiplicacao) 

    return multiplicacao*2