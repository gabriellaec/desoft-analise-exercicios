def calcula_distancia_do_projetil(v,x,y0):
    a=v**2/2*g
    b=1+(1+(2*g*y0)/v**2*(math.sin(x))**2)**(1/2)
    c=math.sin(2*x)
    disatancia=a*b*c
    return distancia