def calcula_velocidade_media(km,hrs):
    vm = km/hrs
    return vm
 
km = int(input('Velocidade: '))
hrs = int(input('Tempo: '))

print(calcula_velocidade_media(km, hrs))