velocidademax= input("Qual a velocidade máxima desta via?")
distancia = input("Qual a distância entre as duas câmeras?")
def multa(tempo1,tempo2):
    
    tempocarro = (velocidademax*1000)/3600
    i = 0
    while i > (-1):
        placa = float(input('Qual a placa do veículo?')
        instante = tempo2 - tempo1             
                      
    
    if instante > tempocarro and instante < tempocarro*1.2:
        return ("O motorista vai ser multado em 130,16 reais.")
    elif instante > tempocarro and instante > tempocarro*1.2 and instante < tempocarro*1.5:
        return ("O motorista vai ser multado em 195,23 reais.")
    elif instante > tempocarro and instante > tempocarro*1.5:
        return ("O motorista vai ser multado em 3 vezes de 195,23 reais e suspenso de dirigir junto à apreensão do documento de habilitação.")
    else:
        return ("O motorista não foi multado")
        
                  