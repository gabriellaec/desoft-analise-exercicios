d=int(input("distância, em km "))
t=int(input("tempo,em horas "))
def calcula_velocidade_media(d,t):
    calcula_velocidade_media = d/t
    return calcula_velocidade_media
print(calcula_velocidade_media(d,t),"Km/h" )