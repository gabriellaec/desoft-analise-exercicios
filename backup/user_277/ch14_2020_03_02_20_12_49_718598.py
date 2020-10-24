def calcula_distancia_do_projetil(v,θ,y0,g):
    a=v**2/2*g
    b=1+(1+(2*g*y0)/v**2*(sin(θ))**2)**(1/2)
    c=sin(2*θ)
    disatancia=a*b*c
    return distancia