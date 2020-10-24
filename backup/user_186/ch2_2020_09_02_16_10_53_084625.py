def calcula_velocidade_media (x, t) :
    y = x/t
    return y
   
 # x é a distância em Km e t é o tempo em h

x = int(input("Qual é a velocidade? " ))
t = int(input("Qual o tempo? " ))
b = calcula_velocidade_media (x, t)
print ("Sua velocidade média foi de:", b, "Km/h")