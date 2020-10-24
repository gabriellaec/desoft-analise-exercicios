n=1
def eh_primo(n):
    if n==0 or n==1:
        return False
    else:
        y=n%2
        while y>=0.5:
            if y==0:
                return False
            else:
                return True
print (eh_primo(n))            

    
   
