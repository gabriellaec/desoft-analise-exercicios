def classifica_triangulo(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            res = "equilátero"
        elif a == b or b == c or c == a:
            res = "isósceles"
        else:
            res = "escaleno"
        return res
    else:
         return "não é triangulo"
