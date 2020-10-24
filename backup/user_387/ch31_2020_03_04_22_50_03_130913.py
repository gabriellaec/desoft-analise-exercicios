def eh_primo(n):


    if n%2 == 0 and n != 2:
        return(False)
    
    elif n == 1:
        return(True)
        
    else:
        a = 3
        while n != a:
            print(a)

            if n%a == 0:
                return(False)
                break

            else:
                a+=2
        
        return(True)
