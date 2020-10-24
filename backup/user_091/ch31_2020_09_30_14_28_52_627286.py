def eh_primo(numero):
    if numero==0:
        return False
    elif numero==1:
        return False
    elif numero==2:
        return True
    elif numero % 2==0 :
        return False
    else:
        i=1
        while(2*i+1)<=numero:
            if numero % (2*i+1)==0:
                return False
            else:
                return True
  

    
    
    