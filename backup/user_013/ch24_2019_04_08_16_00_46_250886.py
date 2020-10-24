def classica_triangulo(a,b,c):
    if a >= b + c or b >= a + c or c >= b + a: 
        return
    if a == b and a == c:
        return "equilátero"
    elif a == b or a == c or b == c:
        return "isóceles"
    else:
        return "escaleno"