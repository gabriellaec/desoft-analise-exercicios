def classifica_triangulo(lado1,lado2 ,lado3):
    if lado1== lado2 and lado2==lado3:
        return 'equilatero'
    elif lado1!=lado2 and lado2==lado3:
        return 'isosceles'
    else:
        return 'escaleno'
    
  
         
    