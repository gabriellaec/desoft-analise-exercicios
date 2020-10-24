def eh_primo(numero):
    i=1
    contador=0
    numero=int(numero)
    if numero%2==0:
        return False
    else:
        while i<numero:
            if numero%i==0:
                contador+=1
            if contador==2:
                return True
            i+=1

