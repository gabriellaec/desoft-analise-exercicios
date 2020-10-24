def calcula_infracao(vel_maxima, dist_cameras, diferenca_instantes):
    #calcula a velocidade do veiculo
    velocidade_metro_seg = float(dist_cameras) / float(diferenca_instantes)
    velocidade_km_hora = velocidade_metro_seg*3.6

    if(velocidade_km_hora > float(vel_maxima)):
        #calcula a porcentagem
        porcentagem = (float(velocidade_km_hora)*100)/float(vel_maxima)
        if(porcentagem < float(20)):
            print("Infração - média;\nPenalidade - multa (R$ 130,16)")
        if((porcentagem > float(20)) & (porcentagem < float(50))):
            print("Infração - grave;\nPenalidade - multa (R$ R$ 195,23)")
        if(porcentagem > float(50)):
            print("Infração - gravíssima;\nPenalidade - multa [três vezes] (3 x R$ 195,23), suspensão imediata do direito de dirigir e apreensão do documento de habilitação.")
    else:
        print("Sem infração")

vel_maxima = input("Velocidade máxima da via em km/h: ") 
dist_cameras = input("Distância em metros entre as duas câmeras: ") 

input_texto=1

veiculo_instantes = {}

while(input_texto == 1):
    placa_veiculo = input("Digite a placa do veiculo: ")

    if(placa_veiculo == ""):
        input_texto = 0

    instante = input("Digite o instante: ") 

    #Segunda camera
    if(placa_veiculo in veiculo_instantes):
        #Calcula a diferença de tempo entre as duas cameras
        diferenca_instantes = float(instante) - float(veiculo_instantes[placa_veiculo])
        calcula_infracao(vel_maxima, dist_cameras, diferenca_instantes)

    #Primeira camera
    else:
        veiculo_instantes[placa_veiculo] = instante