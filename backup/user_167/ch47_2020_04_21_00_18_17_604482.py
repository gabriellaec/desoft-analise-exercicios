def estritamente_crescente (lista1):
    if lista1:
        x= [lista1[0]]
        i=0
        while i < len(lista1):
            y=lista1[i]
            if y>x[-1]:
                x.append(y)
            i+=1
        return x
    else:
        return[]
        

        


        
    
        
            
        
 
        
         
        
        
        