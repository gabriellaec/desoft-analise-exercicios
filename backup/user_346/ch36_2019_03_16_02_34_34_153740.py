def eh_primo(numero):
    
    numero=int(numero)
    if numero==1:
        return False
    elif numero==0:
        return False
    elif numero==2:
        return True
    else:
        i=1
        contador=0
        while i<numero:
            if numero%i==0:
                contador+=1
            if contador==2:
                return True
            i+=1

