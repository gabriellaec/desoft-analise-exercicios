def classifica_triangulo(a,b,c):
    if a==b==c:
        classifica_triangulo=equilátero
     
    if a==b!=c or b==c!=a or a==c!=b:
        classifica_triangulo=isósceles
        
    if a!=b!=c :
        classifica_triangulo=escaleno
        
    return classifica_triangulo 
