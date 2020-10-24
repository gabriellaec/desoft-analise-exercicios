def PiWallis (n):
    
    nominador = 0
    denominador = 1
    conta = 1
    
    for i in range(n):
        if i%2 != 0 :
            nominador += 2
            conta = conta*(nominador/denominador)
            
        if i%2 == 0:
            denomindor += 2
            conta = conta*(nominador/denominador)
            
    pi = conta * 2
    
    return pi