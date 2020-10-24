a =input('Hipotenusa do triangulo: ')
b =input('cateto do triangulo: ')

def encontra_cateto(h,d):
    h = int(a)
    d = int(b)
    c = ((h**2)-(d**2))**0.5
    return c