def classifica_triangulo(a, b, c):
    
    if a == b and b == c: return 'equilátero'
    if a == b or a == c or b == c: return 'escaleno'
    return 'isóceles'