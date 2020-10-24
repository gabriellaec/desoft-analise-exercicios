def PiWallis(num):
    numerador=2
    denominador=1
    i=0
    multi = 1
    
    while i < num:
        multi *= numerador/denominador
        if i%2 == 0:
            denominador += 2
        else:
            numerador += 2
        i+=1
        
    return multi