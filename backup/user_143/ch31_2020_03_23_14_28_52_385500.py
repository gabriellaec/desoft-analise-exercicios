def eh_primo (perg):
    if perg==1 or perg==0:
        return False
    elif perg==2:
        return True
    elif perg>1:
        if perg%2==0:
            return False
        else:
            impar=1
            Invalid=True
            while invalid:
                if impar<=perg and perg%impar ==0:
                    impar+=2
                    return False
                else:
                    return True
                invalid= False
                 
        
        