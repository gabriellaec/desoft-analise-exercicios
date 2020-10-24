def classifica_triangulo(a, b, c):
    if a==b and a==c:
        return 'equilatero'
    elif a!=b and a!=c and b!=c:
        return 'escaleno'
    else:
        return 'isosceles'
print (classifica_triangulo(3,4,5))    
        
        
  
      
       
  
    
    
        
        
