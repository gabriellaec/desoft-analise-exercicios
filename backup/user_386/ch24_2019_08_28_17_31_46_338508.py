clas_tri(a,b,c):
    if a == b and b == c:
        return "equilateral
    elif a != b and b != c:
        return "scalene"
    else:
        return "isosceles"
   