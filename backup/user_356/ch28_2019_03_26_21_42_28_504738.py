v=int(input("Qual a velocidade do seu carro?: "))
if v>80:
    print("Multado! O valor cobrado será de " + str(5*(v-80)))
if v<=80:
    print ("Não foi multado")
