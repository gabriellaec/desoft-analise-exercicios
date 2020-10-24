def eh_primo(numero):
    i=3
    if(numero==2):
        return (True)
    elif(numero%2==0):
        return (False)
    while(i<numero):
        if( numero%i==0 ):
            return (False)
        i+=2
    return True

