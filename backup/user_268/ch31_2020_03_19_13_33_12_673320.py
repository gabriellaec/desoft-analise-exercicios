def eh_primo(n) : 
    if (n <= 1) :
        return False
    if n <=3:
        return True
    if n%2 == 0 or n%3==0:
        return False
    i = 2
    while(i <= n) : 
        if (n % i == 0 and n % (i+1)):
            return False
        i += 1
    else:
         return True
