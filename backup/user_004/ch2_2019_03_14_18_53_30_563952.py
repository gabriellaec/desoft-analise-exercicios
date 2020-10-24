def calcula_velocidade_media(d, h):
    vm=d/h
    return vm

x=int(input('Quantos quilômetros você percorreu? '))
y=int(input('Quantas horas demorou? '))

print(calcula_velocidade_media(x, y))