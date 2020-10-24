def classifica_triangulo(lad1,lad2,lad3):
    if lad1=lad2=lad3:
        return "Equilátero"
    else:
        if lad1=lad3 or lad1=lad2 or lad2=lad3:
            return "Isóceles"
        else:
            return "Escaleno"
        
        
