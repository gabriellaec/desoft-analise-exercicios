def distancia_jaca(v, g, o):
    d=(v**2*(math.sin(math.radians(o))))/g
    if d==100:
        print('Acertou!')
    elif 98<d<102:
        print('Muito perto')
    else:
        print('Muito longe')
    return d
    

a=9.8

b=20

c=30

z=distancia_jaca(b,a,c)
print(z)