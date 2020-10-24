d=int(input("Qual a distância: "))
t=int(input("Qual o tempo: ")) 
def calcula_velocidade_media(distancia,tempo):     
    v=distancia/tempo
    return v

x=calcula_velocidade_media(d,t)            
print(x) 