def encontra_maximo (l):
    i=0
    m=l[0][0]

    while(i<len(l)):
        j=0
        
        while(j<len(l)):
      
          if(l[i][j]>m): 
            m=l[i][j]
            j+=1
    
        i+=1
    
    return m
  
    return m