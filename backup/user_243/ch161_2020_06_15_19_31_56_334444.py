def PiWallis(num):
    numerador=1
    denominador=2
    i=0
    multi = 1
    
    while i < num:
        multi *= numerador/denominador
        if contador%2 == 0:
            denominador += 2
        else:
            nominador += 2
        i+=1
        
    return multi