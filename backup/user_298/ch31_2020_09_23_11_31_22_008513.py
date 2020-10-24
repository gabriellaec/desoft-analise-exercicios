def eh_primo(num):
    nao_primo = True
    t = 2

    if num % t != 0:
        t += 1
        while t < num:
            if num % t != 0:
                t += 2
                 
            
        
            else:
                return False
        
                nao_primo = True
        return True
        nao_primo = False
    else:
        return False
       

print(eh_primo(81))   
