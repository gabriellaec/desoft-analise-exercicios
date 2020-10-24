def classifica_triangulo(a,b,c):
    if a==b==c:
        return "equilátero"
        
    
    elif a==b or b==a or c!=b:
        return "isósceles"
    
    else :
        return "escaleno"
    
    
   