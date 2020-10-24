    
def primos_entre (a,b):
    p=0
    contando=0
    while a<= p and p <= b:
        if p == 0 or p == 1:
            return False
            p+=1
        if p == 2:
            return True
            p+=1
            contando+=1
        if p %2 == 0:
            return False
            p+=1
        else:
            i=3
            while i<p:
                if p%i == 0: 
                    return False
                    i +=2
            return True 
            contando+=1
            p+=1
                
            
        
    