def eh_primo(num):
    nao_primo = True
    t = 2
    if num == 2:
        return True
        
    if num % t != 0 and num != 1:
        t += 1
        while t < num:
            if num % t != 0:
                t += 2
            else:
                return False
        
        return True
        nao_primo = False
    else:
        return False
       

   
