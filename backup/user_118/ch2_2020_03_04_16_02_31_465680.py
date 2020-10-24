def calcula_velocidade_media (vi, vf):
    vm=(vi+vf)/2
    return vm
x=int(input('Velocidade inicial: '))
y=int(input('Velocidade final: '))
z=calcula_velocidade_media (x, y)
print (z)
