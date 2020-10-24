velocidademax= input("Qual a velocidade máxima desta via?")
distancia = input("Qual a distância entre as duas câmeras?")
def multa(tempo1,tempo2):
    tempocamera = tempo2 - tempo1
    tempocarro = (velocidademax*1000)/3600
    
    if tempocamera > tempocarro and tempocamera < tempocarro*1.2:
        return ("O motorista vai ser multado em 130,16 reais.")
    elif tempocamera > tempocarro and tempocamera > tempocarro*1.2 and tempocamera < tempocarro*1.5:
        return ("O motorista vai ser multado em 195,23 reais.")
    elif tempocamera > tempocarro and tempocamera > tempocarro*1.5:
        return ("O motorista vai ser multado em 3 vezes de 195,23 reais e suspenso de dirigir junto à apreensão do documento de habilitação.")
    else:
        return ("O motorista não foi multado")
        
                  