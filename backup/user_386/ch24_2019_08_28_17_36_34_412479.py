def classifica_triangulo (a,b,c):
    if a == b and b == c:
        return "equilateral"
    elif a != b and b != c and a != b: 
        return "scalene"
    else:
        return "isosceles"
   