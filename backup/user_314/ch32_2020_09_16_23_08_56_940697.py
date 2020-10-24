def lista_primos (n):
    i=2
    l_primos=[]
    
    if(n==2):
        l_primos.append("2")
    else:
        while(i<=n):
            j=2
            c=0
            
            while(j<i):
                
                if(i%j==0):
                    c+=1
                
                j+=1        

            if(c==1):
                l_primos.append(i)  
            i+=1
    
    return l_primos