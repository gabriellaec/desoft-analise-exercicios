def eh_primo(n):
    i = 3
    if n<=1:
        return False
    if n%2==0:
        if n==2:
            return True
        else:
            return False
    else:
        while i<n:
            if n%i==0:
                return False
            else:
                i+=2
		return True
   
          
           
      
    