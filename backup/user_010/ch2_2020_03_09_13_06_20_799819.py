def calcula_velocidade_media (x,y):
    y=x/y
    return y
km =int(input("Digite a distância percorrida, em quilômetros: "))
t =int(input("Digite o tempo, em horas: "))
funcao = calcula_velocidade_media (km, t)
print ("A velocidade média é {} km/h".format (funcao))