def area_pentagono(lado):
    altura = (lado**2+(lado/2)**2)**(1/2)
    area = altura * lado / 2
    areatotal = area * 5
    return areatotal