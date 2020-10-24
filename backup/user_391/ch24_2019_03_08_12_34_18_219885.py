def classifica_triangulo(a,b,c):
    if a == b == c:
       res = "equilátero"
    
    elif a == b or b == c or c == a:
        res = "isóceles"
        
    else:
        res = "escaleno"
        
    return res
