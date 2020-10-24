def eh_primo(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    primo = 1
    while primo % n == 0:
        print ("É primo")
        n+=1
        
    
        