def classifica_triangulo(a,b,c):
    if(a == b or a == c or b == c):
        if( a == c and a == b):
            return("equilátero")
    elif( a!= b or a!= c ):
        return("isósceles")
    else:
        return("escaleno")

    
    
