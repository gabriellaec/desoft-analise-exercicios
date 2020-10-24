def classifica_Triangulo (AB,BC,AC):
    if AB == BC == AC:
        return ("equilátero")
    elif AB != BC != AC: 
        return ("escaleno")
    else AB == (BC != AC):
        return ("isósceles")
   