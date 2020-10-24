def eh_primo(x):
    if x==1 or x==0:
        return False
    elif x==2:
        return True
    elif x>1:
        if x%2==0:
            return False 
        else:
            y=3
            invalid=True 
            while invalid:
                if y<x and x%y==0:
                    return False
                elif y==x:
                    return True
                    invalid=False
                y+=2
def primos_entre(a, b):
    p=0
    i=0
    while p<a or p>b:
        p+=1
    while p>=a and p<=b:
        if eh_primo(p):
            p+=1
            i+=1
        else:
            p+=1
    return i
      
    
    