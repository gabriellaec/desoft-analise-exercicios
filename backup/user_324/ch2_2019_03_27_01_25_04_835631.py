def calcula_velocidade_media(distancia,tempo):     
    v=distancia/tempo
    return v


d=input("Qual a distância: ")
t=input("Qual o tempo: ")
 

x=calcula_velocidade_media(d,t)            
print(x)