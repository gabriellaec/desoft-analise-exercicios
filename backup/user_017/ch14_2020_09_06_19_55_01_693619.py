def calcula_distancia_do_projetil(v,y0,x):
    d= ((v**2)/2*9,8)*(1+(1 + ((2*9,8*y0)/(v**2 * (math.sin(x))**2))**0,5) * math.sin(2x)
    return d
a= 10
b=50                       
c=30
f=calcula_distancia_do_projetil(a,b,c)    
print (f)