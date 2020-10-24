def verifica_primo(numero):
    if numero == 2:
        return True
    elif numero %2 == 0 or numero <= 1:
        return False
    else:
        contador=3
        divisores=1
        while contador <= numero:
            if numero %contador == 0:
                divisores +=1
            contador +=2
        if divisores > 2:
            return False
        else:
            return True
        
    