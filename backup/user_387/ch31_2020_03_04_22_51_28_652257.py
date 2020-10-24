def eh_primo(n):


    if n%2 == 0 and n != 2:
        return(False)
    
    if n == 1 or n == 0:
        return(False)
        
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
