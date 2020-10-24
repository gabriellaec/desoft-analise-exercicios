def encontra_maximo (l):
    i=0
    m=abs(l[0][0])

    while(i<len(l)):
        j=0
        
        while(j<len(l)):
      
            if(abs(l[i][j])>m): 
                m=abs(l[i][j])
          
            j+=1
    
        i+=1
    
    return m
  