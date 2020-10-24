def classifica_triangulo(l1, l2, l3):
    classi = 0 
    
    if l1==l2 and l2==l3:
        classi =  "equilátero"
    elif l1 == l2 or l1==l3 or l2==l3:
        classi = "isósceles"
    else:
        classi = "escaleno"
        
    return classi
        