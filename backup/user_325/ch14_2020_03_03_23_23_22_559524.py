def calcula_distancia_do_projetil(v,o,yo):
    d = ((v**2)/(2*9.8))*(1+(1+(2*9.8*yo)/(v**2)*math.sin(o)**2)**(1/2)*math.sin(2*o)
    return d
print(calcula_distancia_do_projetil(10,45,0)