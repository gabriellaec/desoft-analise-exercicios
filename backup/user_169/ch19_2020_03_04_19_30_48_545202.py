def classifica_triangulo(a,b,c):
    if a==b==c:
        return "equilátero"
        
    
    elif a==b or c==a or c==b:
        return "isósceles"
    
    else:
        return "escaleno"
    
    
   