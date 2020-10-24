def primos_entre(a,b):
    i=1
    numero>=a and numero<=b
    if(numero==2):
        return (True)
    elif(numero%2==0):
        return (False)
    while(i<numero):
        if( numero%i==0 ):
            return (False)
        i+=2
    return True

