velocidade_maxima=float(input("Digite a velocidade máxima (km/h) da via: ")) 
distancia=float(input("Digite a distancia entre as duas cameras: "))


GAME=True
while GAME == True:
    
    placa=input("Digite sua placa de 7 caracteres: ")
    if placa=="":
        GAME==False 
    
    instante=float(input("Digite o instante (em segundos) em que passou pela camera: "))
    
    placa_1=input("Digite sua placa de 7 caracteres: ")
    
    novo_instante=float(input("Digite o instante (em segundos) em que passou pela nova camera: "))
    
    if placa==placa_1:
    
        velocidade = (distancia/(novo_instante-instante))*3.6
        if velocidade < 1.2*velocidade_maxima and velocidade >= velocidade_maxima:
            print("Voce tomou uma multa de infração média, penalidade de R$130,16")
    
        elif velocidade >= 1.2*velocidade_maxima and velocidade < 1.5*velocidade_maxima:
            print("Voce tomou uma multa de infração média, penalidade de R$130,16")
        
        elif velocidade >= 1.5*velocidade_maxima:
            print("Voce tomou uma multa de infração gravissima, sua penalidade será de R$585,69 e terá sua cnh caçada")
    
        else:
            print ("Voce nao tomou multa")
