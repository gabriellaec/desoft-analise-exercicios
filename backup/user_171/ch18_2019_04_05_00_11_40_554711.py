cat=int(input("cateto 1: "))
hip=int(input("hipotenusa: "))
def encontra_cateto(c):
    c=((hip**2)/(cat**2))**0.5
    return c
