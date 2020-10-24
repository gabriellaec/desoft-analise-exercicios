import random
vmax=int(input("Qual eh a velocidade maxima permitida?:"))
dcam=int(input("Qual eh a distancia entre as cameras?:"))
CaracteresDisponiveis=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i=0
tempo=0
numEntradas=[]
PlacaCarro=[0]*7
while i == 0:
    tempo+=1
    random.shuffle(CaracteresDisponiveis)
    for j in range(7):
        PlacaCarro[j]=CaracteresDisponiveis[j]
    numEntradas.append(tempo)
    if len(numEntradas) == 2:
        Dcarro= numEntradas[1]-numEntradas[0]
        if Dcarro<=vmax*1.2:
            print("Nada de errado com o veiculo de Placa{0}".format(PlacaCarro))            
        elif Dcarro > vmax*1.2:
            multa=130.16
        elif Dcarro >vmax*1.5:
            multa= (195.23)*3
        else:
            multa=195.23
        print("Motorista do carro {0}, recebeu uma multa de {1}".format(PlacaCarro,multa))
        numEntradas=[]
    PlacaCarro=[]

