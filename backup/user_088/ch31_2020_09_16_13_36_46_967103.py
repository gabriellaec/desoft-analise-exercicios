def eh_primo(numero):
    i=0
    while(True):
        if(numero!=2 and numero%2==0 and numero%i==0 ):
            return False
        else:
            return True
    i+=1