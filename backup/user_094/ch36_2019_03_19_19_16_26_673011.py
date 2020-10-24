i=3
def eh_primo(x):
    if x==1 or x==0: 
        return False
    elif x==2:
        return True
    else:
        while i<x:
            if x%i != 0:
                i+=2
            else:
                return False
		return True
          
   