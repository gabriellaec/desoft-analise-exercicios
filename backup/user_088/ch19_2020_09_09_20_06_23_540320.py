def classifica_triangulo(lado1,lado2 ,lado3):
    if lado1== lado2 and lado2==lado3:
        return 'O triangulo é equilatero'
    elif lado1!=lado2 and lado2==lado3:
        return 'o triangulo é isosceles'
    else:
        return 'o triangulo é escaleno'
  
         
    