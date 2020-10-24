def eh_primo(num):
    if num == 0 or num == 1:
        return False
    else:
        if num == 2:
            return True
        elif num%2 == 0:
            return False
        else:
            x = 3
            while(x < num):
                if num % x == 0:
                    break
                x = x + 2
            if x == num:
                return True
            else:
                return False
def primos_entre(a,b):
    i=a
    qtd=0
    primos=[]
    while i<=b:
        if eh_primo(i)==True:
            qtd+=1
            primos.append(eh_primo[i])
        i+=1
    return primos
        
            
            
            
      
       
    
    