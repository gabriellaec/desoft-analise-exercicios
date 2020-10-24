def classifica_triangulo(lad1,lad2,lad3):
    if lad1=lad2=lad3:
        return "equilátero"
    else:
        if lad1=lad3 or lad1=lad2 or lad2=lad3:
            return "isóceles"
        else:
            return "escaleno"
        
        
